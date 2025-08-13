import ctypes
from ctypes import *
from ctypes import CDLL

class HawtC:

    """
    HawtC类，用于调用HawtC.dll中的INIMain函数
    """
    def __init__(self, dll_path):
        print(dll_path)
        self.dll=CDLL(dll_path)
        
    def HawtC_S_INI(self,path):
        """
        用于调用HawtC.dll中的HawtC_S_Simulation_INI函数,读取运行文件,并完成初始化和运行工作.该模式下无法运行MoptL模式
        """
        config_path=path
        config_path_bytes = config_path.encode('utf-8')
        # 将字符串转换为字符指针
        config_path_ptr = ctypes.c_char_p(config_path_bytes)
        # 调用函数
        self.dll.HawtC_S_INI(config_path_ptr)
        
    def HawtC_S_Close(self,turbinenum):
        """
        用于调用HawtC.dll中的Close函数,释放内存
        """     
        turbinenum =ctypes.c_int(turbinenum)   
        self.dll.HawtC_S_Close(turbinenum)
        

    def HawtC_S_Update_Step(self,times_n,t):
        """
        用于调用HawtC.dll中的Update函数,进行时间步进
        """
        self.dll.HawtC_S_Update_Step.argtypes = [ ctypes.c_int, ctypes.c_double]
        self.dll.HawtC_S_Update_Step.restype = None
        self.dll.HawtC_S_Update_Step(times_n,t)

    def HawtC_Solve(self):
        """
        用于调用HawtC.dll中的求解函数,不能自定义时间步进
        """        


        self.dll.HawtC_S_Solve()
        
    def HawtC_S_GetTowerBaseFx(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetTowerBaseFx函数,获取塔基X方向的力
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetTowerBaseFx.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetTowerBaseFx(num)
        
    def HawtC_S_GetTowerBaseFy(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetTowerBaseFy函数,获取塔基Y方向的力
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetTowerBaseFy.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetTowerBaseFy(num)
        
    def HawtC_S_GetTowerBaseFz(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetTowerBaseFz函数,获取塔基Z方向的力
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetTowerBaseFz.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetTowerBaseFz(num)
        
    def HawtC_S_GetTowerBaseMx(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetTowerBaseMx函数,获取塔基X方向的力矩
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetTowerBaseMx.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetTowerBaseMx(num)
        
    def HawtC_S_GetTowerBaseMy(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetTowerBaseMy函数,获取塔基Y方向的力矩
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetTowerBaseMy.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetTowerBaseMy(num)
        
    def HawtC_S_GetTowerBaseMz(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetTowerBaseMz函数,获取塔基Z方向的力矩
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetTowerBaseMz.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetTowerBaseMz(num)
        
    def HawtC_S_GetLocalTowerMxLoads(self,turbnum,J):
        """
        用于调用HawtC.dll中的HawtC_S_GetLocalTowerMxLoads函数,获取塔架各节点X方向的力矩
        """
        J =ctypes.c_int(J)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetLocalTowerMxLoads.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetLocalTowerMxLoads(num,J)
        
        
    def HawtC_S_GetLocalTowerMyLoads(self,turbnum,J):
        """
        用于调用HawtC.dll中的HawtC_S_GetLocalTowerMyLoads函数,获取塔架各节点Y方向的力矩
        """
        J =ctypes.c_int(J)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetLocalTowerMyLoads.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetLocalTowerMyLoads(num,J)
        
    def HawtC_S_GetLocalTowerMzLoads(self,turbnum,J):
        """
        用于调用HawtC.dll中的HawtC_S_GetLocalTowerMzLoads函数,获取塔架各节点Z方向的力矩
        """
        J =ctypes.c_int(J)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetLocalTowerMzLoads.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetLocalTowerMzLoads(num,J)
        
    def HawtC_S_GetLocalTowerFxLoads(self,turbnum,J):
        """
        用于调用HawtC.dll中的HawtC_S_GetLocalTowerFxLoads函数,获取塔架各节点X方向的力
        """
        J =ctypes.c_int(J)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetLocalTowerFxLoads.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetLocalTowerFxLoads(num,J)
        
    def HawtC_S_GetLocalTowerFyLoads(self,turbnum,J):
        """
        用于调用HawtC.dll中的HawtC_S_GetLocalTowerFyLoads函数,获取塔架各节点Y方向的力
        """
        J =ctypes.c_int(J)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetLocalTowerFyLoads.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetLocalTowerFyLoads(num,J)
        
    def HawtC_S_GetLocalTowerFzLoads(self,turbnum,J):
        """
        用于调用HawtC.dll中的HawtC_S_GetLocalTowerFzLoads函数,获取塔架各节点Z方向的力
        """
        J =ctypes.c_int(J)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetLocalTowerFzLoads.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetLocalTowerFzLoads(num,J)
        
        
    def HawtC_S_GetBladeRootFx(self,turbnum,blade):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeRootFx函数,获取叶片根X方向的力
        """
        blade =ctypes.c_int(blade)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeRootFx.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeRootFx(num,blade)
        
    def HawtC_S_GetBladeRootFy(self,turbnum,blade):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeRootFy函数,获取叶片根Y方向的力
        """
        blade =ctypes.c_int(blade)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeRootFy.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeRootFy(num,blade)
        
    def HawtC_S_GetBladeRootFz(self,turbnum,blade):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeRootFz函数,获取叶片根Z方向的力
        """
        blade =ctypes.c_int(blade)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeRootFz.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeRootFz(num,blade)
        
    def HawtC_S_GetBladeRootMx(self,turbnum,blade):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeRootMx函数,获取叶片根X方向的力矩
        """
        blade1 =ctypes.c_int(blade)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeRootMx.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeRootMx(num,blade1)
        
    def HawtC_S_GetBladeRootMy(self,turbnum,blade):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeRootMy函数,获取叶片根Y方向的力矩
        """
        blade1 =ctypes.c_int(blade)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeRootMy.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeRootMy(num,blade1)
        
    def HawtC_S_GetBladeRootMz(self,turbnum,blade):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeRootMz函数,获取叶片根Z方向的力矩
        """
        blade1 =ctypes.c_int(blade)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeRootMz.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeRootMz(num,blade1)
        
    def HawtC_S_GetBladeLocalMx(self,turbnum,blade,section):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeLocalMx函数,获取叶片各节根X方向的力矩
        """
        blade1 =ctypes.c_int(blade)
        section1 =ctypes.c_int(section)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeLocalMx.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeLocalMx(num,blade1,section1)
        
    def HawtC_S_GetBladeLocalMy(self,turbnum,blade,section):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeLocalMy函数,获取叶片各节根Y方向的力矩
        """
        blade1 =ctypes.c_int(blade)
        section1 =ctypes.c_int(section)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeLocalMy.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeLocalMy(num,blade1,section1)
        
    def HawtC_S_GetBladeLocalMz(self,turbnum,blade,section):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeLocalMz函数,获取叶片各节根Z方向的力矩
        """
        blade =ctypes.c_int(blade)
        section =ctypes.c_int(section)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeLocalMz.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeLocalMz(num,blade,section)
        
    def HawtC_S_GetBladeLocalFx(self,turbnum,blade,section):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeLocalFx函数,获取叶片各节根X方向的力
        """
        blade =ctypes.c_int(blade)
        section =ctypes.c_int(section)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeLocalFx.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeLocalFx(num,blade,section)

    def HawtC_S_GetBladeLocalFy(self,turbnum,blade,section):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeLocalFy函数,获取叶片各节根Y方向的力
        """
        blade =ctypes.c_int(blade)
        section =ctypes.c_int(section)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeLocalFy.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeLocalFy(num,blade,section)
        
    def HawtC_S_GetBladeLocalFz(self,turbnum,blade,section):
        """
        用于调用HawtC.dll中的HawtC_S_GetBladeLocalFz函数,获取叶片各节根Z方向的力
        """
        blade =ctypes.c_int(blade)
        section =ctypes.c_int(section)
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetBladeLocalFz.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetBladeLocalFz(num,blade,section)
        
    def HawtC_S_GetPlatformSurge(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformSurge函数,获取平台 surge方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformSurge.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformSurge(num)
        
    def HawtC_S_GetPlatformSway(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformSway函数,获取平台 sway方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformSway.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformSway(num)
        
    def HawtC_S_GetPlatformHeave(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformHeave函数,获取平台 heave方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformHeave.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformHeave(num)
        
    def HawtC_S_GetPlatformRoll(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformRoll函数,获取平台 roll方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformRoll.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformRoll(num)
        
    def HawtC_S_GetPlatformPitch(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformPitch函数,获取平台 pitch方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformPitch.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformPitch(num)
        
    def HawtC_S_GetPlatformYaw(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformYaw函数,获取平台 yaw方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformYaw.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformYaw(num)
        
    def HawtC_S_GetPlatformSurgeVel(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformSurge函数,获取平台 surge方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformSurgeVel.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformSurgeVel(num)
        
    def HawtC_S_GetPlatformSwayVel(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformSway函数,获取平台 sway方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformSwayVel.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformSwayVel(num)
        
    def HawtC_S_GetPlatformHeaveVel(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformHeave函数,获取平台 heave方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformHeaveVel.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformHeaveVel(num)
        
    def HawtC_S_GetPlatformRollVel(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformRoll函数,获取平台 roll方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformRollVel.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformRollVel(num)
        
    def HawtC_S_GetPlatformPitchVel(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformPitch函数,获取平台 pitch方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformPitchVel.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformPitchVel(num)
        
    def HawtC_S_GetPlatformYawVel(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformYaw函数,获取平台 yaw方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformYawVel.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformYawVel(num)
    
    
    def HawtC_S_GetPlatformSurgeAcc(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformSurge函数,获取平台 surge方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformSurgeAcc.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformSurgeAcc(num)
        
    def HawtC_S_GetPlatformSwayAcc(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformSway函数,获取平台 sway方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformSwayAcc.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformSwayAcc(num)
        
    def HawtC_S_GetPlatformHeaveAcc(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformHeave函数,获取平台 heave方向的位移
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformHeaveAcc.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformHeaveAcc(num)
        
    def HawtC_S_GetPlatformRollAcc(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformRoll函数,获取平台 roll方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformRollAcc.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformRollAcc(num)
        
    def HawtC_S_GetPlatformPitchAcc(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformPitch函数,获取平台 pitch方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformPitchAcc.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformPitchAcc(num)
        
    def HawtC_S_GetPlatformYawAcc(self,turbnum):
        """
        用于调用HawtC.dll中的HawtC_S_GetPlatformYaw函数,获取平台 yaw方向的旋转
        """
        num =ctypes.c_int(turbnum)
        self.dll.HawtC_S_GetPlatformYawAcc.restype = ctypes.c_double
        return  self.dll.HawtC_S_GetPlatformYawAcc(num)
          
    class Test:
        """
        用于测试HawtC.dll中的测试函数
        """
        def __init__(self,MBD):
            self.dll=MBD
        
        def GetAddc(self,a,b):
            """
            用于调用HawtC.dll中的GetAddc函数,获取平台 yaw方向的旋转
            """
            get_addc=self.dll.GetAddc
            self.dll.GetAddc.restype = ctypes.c_void_p
            AddcType = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
            addc_from_MBD = ctypes.cast(self.dll.GetAddc(), AddcType)
            addc_from_MBD.restype = ctypes.c_double
            a=ctypes.c_double(a)
            b=ctypes.c_double(b)
            return addc_from_MBD(a,b)
        
        def  SetAddc(self,add_func):
            # 创建 Python 委托
            AddcType = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
            addc_delegate = AddcType(add_func)
            self.dll.SetAddc.argtypes = [ctypes.c_void_p]  # 设置参数类型
            # 将 Python 委托传递给 C# MBD
            self.dll.SetAddc(ctypes.cast(addc_delegate, ctypes.c_void_p))
    
    