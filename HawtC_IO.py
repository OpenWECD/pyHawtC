import os
import re
import datetime
import logging
from typing import List, Dict, Optional, Union, Tuple, Any

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('YML')

class YML:
    """处理YAML文件的读写和操作，支持节点增删改查和层级结构管理"""
    
    # 类常量
    
    YML_VERSION = "2.0.013"
    
    
    #所有行
    lines = []  # 存储YAML文件的行
    
    #当前层级
    tier = 0  # 当前节点层级
    
    
    nodeList = []  # 存储所有节点的列表
    
    path = ""  # YAML文件路径
    
    class Node:
        """表示YAML文件中的节点"""
        __slots__ = ('name', 'value', 'parent', 'space', 'tier')
        
        def __init__(self, name: str = "", value: str = None,  # type: ignore
                     parent: 'YML.Node' = None, space: int = 0, tier: int = 0):
            self.name = name
            self.value = value
            self.parent = parent
            self.space = space  # 缩进空格数
            self.tier = tier    # 节点层级
            
        def clone(self) -> 'YML.Node':
            """创建节点的深拷贝"""
        
            cloned_parent = self.parent.clone() if self.parent else None
            return YML.Node(
                name=self.name,
                value=self.value,
                parent=cloned_parent,
                space=self.space,
                tier=self.tier
            )
            
        def __repr__(self) -> str:
            return f"<Node '{self.name}': {self.value}>"

    def __init__(self, path: str = None):
        """
        初始化YAML处理器
        :param path: YAML文件路径，若为None则创建空结构
        """
        self.lines: List[str] = []
        self.tier: int = 0
        self.node_list: List[YML.Node] = []
        self.path: str = path
        
        if path:
            # 读取文件内容
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    self.lines = f.read().splitlines()
            else:
                self.lines = ["# OpenWECD.IO.IO Yaml by 赵子祯@zzz，will create file!"]
            
            # 解析YAML内容
            self._parse_lines()
            
            # 添加元数据节点
            self._add_metadata_nodes()

    def _parse_lines(self):
        """解析YAML文本行并构建节点树"""
        current_indent = -1
        currentNode = None
        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            stripped_line = line.strip()
            
            # 跳过空行和注释
            if not stripped_line or stripped_line.startswith('#'):
                i += 1
                continue
                
            # 检查是否为有效节点
            if ':' not in line:
                i += 1
                continue
                
            # 分割键值对
            kv = line.split(':', 1)
            if not kv:
                i += 1
                continue
                
            # 创建节点
            node = YML.Node()
            node.space = self._find_pre_space(line)
            node.name = kv[0].strip()
            
            # 处理值
            if len(kv) > 1:
                value_part = kv[1].strip()
                if not value_part:  # 值为空的情况
                    node.value = self._read_multiline_value(i, node.space)
                    # 跳过已处理的行
                    if node.value and '\n' in node.value:
                        i += node.value.count('\n')
                else:
                    node.value = value_part
            else:
                node.value = None
                
            # 设置父节点
            node.parent = self._find_parent(node.space)
            self.node_list.append(node)
            i += 1

    def _read_multiline_value(self, start_index: int, base_indent: int) -> str:
        """
        读取多行值
        :param start_index: 起始行索引
        :param base_indent: 基础缩进量
        :return: 拼接后的多行值
        """
        values = []
        j = start_index + 1
        
        while j < len(self.lines):
            line = self.lines[j]
            if not line.strip():
                j += 1
                continue
                
            # 检查缩进层级
            indent_pos = line.find('-  ')
            if indent_pos == -1:
                break
                
            indent_level = len(line[:indent_pos])
            if base_indent + 1 <= indent_level <= base_indent + 3:
                values.append(line.strip())
                j += 1
            else:
                break
                
        return '\n'.join(values) if values else None

    def _add_metadata_nodes(self):
        """添加元数据节点"""
        # 检查并添加版本信息
        version_key = "OpenWECD.Information.YMLVersion"
        if not self.check_node_exists(version_key):
            self.add_node(version_key, self.YML_VERSION)
        else:
            self._validate_yml_version()
            
        # 添加作者信息
        self.add_node("OpenWECD.Information.Auther", "YML 模块由赵子祯独立开发 @copyright")
        
        # 添加修改时间
        self.add_node("OpenWECD.Information.最后修改时间", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        # 格式化节点结构
        self.formatting()

    def _validate_yml_version(self):
        """验证YML版本兼容性"""
        version_key = "OpenWECD.Information.YMLVersion"
        stored_version = self.read(version_key)
        
        if stored_version:
            stored_parts = [int(x) for x in stored_version.split('.') if x]
            current_parts = [int(x) for x in self.YML_VERSION.split('.') if x]
            
            if stored_parts[0] != current_parts[0] or \
               stored_parts[1] != current_parts[1]:
                logger.error(
                    f"不兼容的YML版本: {stored_version}，当前程序支持 {self.YML_VERSION}"
                )

    def clone(self) -> 'YML':
        """创建YML对象的深拷贝"""
        cloned = YML()
        cloned.tier = self.tier
        cloned.lines = self.lines.copy()
        cloned.node_list = [node.clone() for node in self.node_list]
        cloned.path = self.path
        return cloned

    def modify(self, key: str, value: str):
        """修改指定节点的值"""
        node = self.find_node_by_key(key)
        if node:
            node.value = value

    def read(self, key: str) -> str:
        """读取指定节点的值"""
        node = self.find_node_by_key(key)
        return node.value if node else ""

    def find_node_by_key(self, key: str) -> Optional[Node]:
        """
        通过键路径查找节点
        :param key: 点分隔的键路径 (e.g., "parent.child.grandchild")
        :return: 找到的节点或None
        """
        keys = key.split('.')
        for node in reversed(self.node_list):  # 从后向前搜索
            if node.name == keys[-1]:
                # 检查父级匹配
                temp = node
                match_count = 1
                for key_part in reversed(keys[:-1]):
                    if temp.parent and temp.parent.name == key_part:
                        match_count += 1
                        temp = temp.parent
                    else:
                        break
                if match_count == len(keys):
                    return node
        return None

    def check_node_exists(self, key: str) -> bool:
        """检查节点是否存在"""
        return self.find_node_by_key(key) is not None

    def get_node_key(self, node: Node) -> str:
        """获取节点的完整键路径"""
        if not node.parent:
            return node.name
        return f"{self.get_node_key(node.parent)}.{node.name}"

    def add_node(self, key: str, value: str = None):
        """
        添加新节点
        :param key: 点分隔的键路径
        :param value: 节点值
        """
        # 已存在则更新
        if self.check_node_exists(key):
            self.modify(key, value)
            return
            
        keys = key.split('.')
        # 单节点情况
        if len(keys) == 1:
            self._add_child_node(None, keys[0], value)
        else:
            # 确保父路径存在
            for i in range(1, len(keys)):
                parent_key = '.'.join(keys[:i])
                if not self.check_node_exists(parent_key):
                    self._add_child_node('.'.join(keys[:i-1]), keys[i-1], None)
                    
            # 添加最终节点
            parent_key = '.'.join(keys[:-1])
            self._add_child_node(parent_key, keys[-1], value)

    def _add_child_node(self, parent_key: Optional[str], name: str, value: str):
        """添加子节点到指定父节点"""
        # 根节点
        if parent_key is None:
            new_node = YML.Node(name=name, value=value, space=0)
            self.node_list.append(new_node)
        else:
            parent_node = self.find_node_by_key(parent_key)
            if parent_node:
                print(f"添加子节点: {name} 到父节点: {parent_node.name}")
            else:
                new_node = YML.Node(
                    name=name,
                    value=value,
                    parent=parent_node,
                    space=parent_node.space + 2,
                    tier=parent_node.tier + 1
                )
                self.node_list.append(new_node)

    def delete_node(self, key: str):
        """删除节点及其所有子节点"""
        node_to_delete = self.find_node_by_key(key)
        if not node_to_delete:
            logger.warning(f"未找到要删除的节点: {key}")
            return
            
        nodes_to_remove = []
        self._find_all_children(node_to_delete, nodes_to_remove)
        
        # 移除节点
        for node in nodes_to_remove:
            if node in self.node_list:
                self.node_list.remove(node)
                
        self.formatting()

    def _find_all_children(self, parent: Node, nodes: List[Node]):
        """递归查找所有子节点"""
        children = [node for node in self.node_list if node.parent == parent]
        for child in children:
            nodes.append(child)
            self._find_all_children(child, nodes)

    def find_children(self, key: str) -> List[Node]:
        """查找指定节点的直接子节点"""
        parent = self.find_node_by_key(key)
        if not parent:
            logger.error(f"未找到父节点: {key}")
            return []
            
        return [node for node in self.node_list if node.parent == parent]

    def save(self, save_path: str = None, format_output: bool = True):
        """保存YAML到文件"""
        path = save_path or self.path
        if not path:
            logger.error("未指定保存路径")
            return
            
        # 确保目录存在
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        # 格式化节点
        if format_output:
            self.formatting()
            
        # 写入文件
        with open(path, 'w', encoding='utf-8') as f:
            for node in self.node_list:
                indent = '  ' * node.tier
                line = f"{indent}{node.name}:"
                if node.value:
                    # 多行值处理
                    if '\n' in node.value:
                        lines = node.value.split('\n')
                        f.write(f"{line}\n")
                        for sub_line in lines:
                            f.write(f"{indent}  - {sub_line.strip()}\n")
                    else:
                        f.write(f"{line} {node.value}\n")
                else:
                    f.write(f"{line}\n")

    def formatting(self):
        """重新格式化节点列表（按层级排序）"""
        # 查找根节点
        root_nodes = [node for node in self.node_list if node.parent is None]
        
        # 递归添加子节点
        formatted_nodes = []
        for node in root_nodes:
            formatted_nodes.append(node)
            self._collect_children(node, formatted_nodes)
            
        self.node_list = formatted_nodes

    def _collect_children(self, parent: Node, nodes: List[Node]):
        """递归收集子节点"""
        children = [node for node in self.node_list if node.parent == parent]
        for child in children:
            child.tier = parent.tier + 1
            nodes.append(child)
            self._collect_children(child, nodes)

    @staticmethod
    def _find_pre_space(line: str) -> int:
        """计算行首空格数"""
        return len(line) - len(line.lstrip())

    def _find_parent(self, space: int) -> Optional[Node]:
        """根据缩进查找父节点"""
        if not self.node_list:
            return None
            
        # 反向查找最近的缩进较小的节点
        for node in reversed(self.node_list):
            if node.space < space:
                return node
        return None

# 示例用法
if __name__ == "__main__":
    # 创建YAML处理器
    yml = YML("./config.yml")
    
    # # 添加新配置
    # yml.add_node("database.host", "localhost")
    # yml.add_node("database.port", "5432")
    # yml.add_node("database.credentials.username", "admin")
    
    # # 修改现有值
    # yml.modify("database.port", "5433")
    
    # # 读取值
    # print("数据库端口:", yml.read("database.port"))
    
    # # 删除节点
    # yml.delete_node("database.credentials")
    
    # 保存到文件
    # yml.save("./config.yml")