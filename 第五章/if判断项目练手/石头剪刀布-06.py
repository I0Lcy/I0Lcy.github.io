# 综合应用
# 目标：
# 1 强化 多个条件 的 逻辑运算
# 2 体会import 导入模块 ("工具包") 的使用

# 需求：
# 1 从控制台输入要出的拳 -- 石头(1) / 剪刀(2) / 布(3) /
# 2 电脑 随机 出拳 -- 先假定电脑只会出石头，完成整体代码的功能
# 3 比较胜负

# 序号   规则
# 1      石头 胜 剪刀
# 2      剪刀 胜 布
# 3      布 胜 石头

import random
player = int(input("请出拳 石头(1) / 剪刀(2) / 布(3): "))

computer = random.randint(1, 3)  # 利用模块生成1-3(包括1-3)的随机数
print(computer)  # 主要想看下生成的数字
if ((player == 1 and computer == 2) # 将需求中要求的规则写出来，只要其中一个成立了，就输出赢了
        or (player == 2 and computer == 3) 
        or (player == 3 and computer == 1)):
        print("赢了")
elif player == computer:  # 这里，如果电脑和玩家出的拳一样的情况
    print("心有灵犀，继续玩")
else:  # 如果上面都不成立，那么else语句则执行玩家失败后的语句
    print("决战到天亮")