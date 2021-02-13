# # # # 计算 0 - 100 之间 所有 偶数 的累计求和结果
# # 偶数是能够被2所整除的整数

# # # # 开发步骤
# # # 1. 编写循环 确认 要计算的数字
# # # 2. 添加结果 变量, 在循环体内部处理计算结果

# # 0-100之间偶数相加的结果

# NumberOne = 0
# numberTwo = 0

# while NumberOne <= 100:
#     if NumberOne % 2 == 0:
#         numberTwo += NumberOne
#     NumberOne += 1
# print("0-100之间所有偶数相加结果: %d" % numberTwo)

# # 0-100奇数相加结果
# # 技术就是不是2的倍数，奇数指不能被2整除的整数

NumberOne = 0
numberTwo = 0

while NumberOne <= 100:
    if NumberOne % 2 != 0:
        numberTwo += NumberOne
    NumberOne += 1
print("0-100之间所有奇数相加结果: %d" % numberTwo)
