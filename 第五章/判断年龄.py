# 初代
age = 18
if age >= 18:
    print("可以去网吧海皮!")
else:
    print("年龄不到，不能去网吧海皮!")

# 改进，让用户输入自己的年龄

age = input("请输入您的年龄: ")

if age >= str(18):    # 在这里将18转换为字符串(str)类型，与用户输入的年龄作比较
    print("可以去网吧海皮")
else:
    print("不可以去网吧海皮")

# 改进增强版
age = int(input("请输入您的年龄: "))#在这里将用户输入的年龄使用int转换成数字型


if age >= 18:
    print("可以去网吧")
else:
    print("不可以去网吧")