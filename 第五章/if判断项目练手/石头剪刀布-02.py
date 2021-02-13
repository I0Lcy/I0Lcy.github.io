# 需求：
# 1 从控制台输入要出的拳头 -- 石头(1) / 剪刀(2) / 布(3) /
# 2 电脑 随机 出拳 -- 先假定电脑只会出石头，完整整体代码功能
# 3 比较胜负

player = int(input("请输入您要出的拳 - 石头(1) / 剪刀(2) / 布(3): "))

computer = 1
print("玩家出的拳是: %d - 电脑出的拳是 %d" % (player, computer))
if player == 1:
    print("平局，重新开始游戏")
elif player == 2:
    print("输了，重新开始游戏")
elif player == 3:
    print("赢了, 欧皇啊")

