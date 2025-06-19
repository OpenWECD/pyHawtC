# 我们基于HawtC_c_dll.实现python调用
class YML:
    def __init__(self, path):
        self.path = path

    def load(self):
        import yaml
        with open(self.path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
