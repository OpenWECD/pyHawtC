import HawtC_S_Simulation as hsim

# 导入HawtC dll 文件
sim = hsim.HawtC(r"G:\2026\HawtC2\build\HawtC2_User_C.dll")

# # 初始化仿真模型
# sim.HawtC_S_INI(r"G:\2026\HawtC2\demo\5MW_Spar\HawtC2_5MW_PowerProduction_Spar.hst")
# # 直接求解模型
# sim.HawtC_Solve()
# # 关闭仿真
# sim.HawtC_S_Close(0)

###################### DEMO 2 步长控制来首先求解 ###############################
# 初始化仿真模型
sim.HawtC_S_INI(r"G:\2026\HawtC2\demo\5MW_Spar\HawtC2_5MW_PowerProduction_Spar.hst")

dt  = 0.05
t = 0
for i in range(1000):
    t=t + dt
    sim.HawtC_S_Update_Step(i,t)
    Fx=sim.HawtC_S_GetBladeLocalFx(0,1,0)
    print(Fx)
# 关闭仿真
sim.HawtC_S_Close(0)