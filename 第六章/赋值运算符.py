# # 在 python 中，使用 = 可以给变量赋值
# 在算数运算时，为了简化代码的编写，python 还提供了一系列的 与 算术运算符 对应的 赋值运算符
# 注意：赋值运算符 中间不能使用空格

# 下面是一些常用的：
# 简单的赋值运算符 c = a + b 将 a + b 的运算结果赋值为 c
# 加法赋值运算符 c += a 等效于 c = c + a
# 减法赋值运算符 c -= a 等效于 c = c - a
# 乘法赋值运算符 c *= a 等效于 c = c * a
# 除法赋值运算符 c /= a 等效于 c = c / a
# 取模赋值运算符 c %= a 等效于 c = c % a

# 第三节代码改进，使用赋值运算符
# 原:
NumberStrings = 1

while NumberStrings < 5:
    print("Hello wolrd")
    NumberStrings = NumberStrings + 1

print("第一个程序循环结束后: %d" % NumberStrings)

# 改进：

NumberStr = 1

while NumberStr < 5:
    print("Hello world")
    NumberStr += 1

print("第二个程序结束后: %d" % NumberStr)