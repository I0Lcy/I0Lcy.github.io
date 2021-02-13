# 需求：打印九九乘法表
# 开发步骤：
# 1.打印9行小星星

Num = 1

while Num <= 9:
    col = 1
    while col <= Num:
        print("*", end="")
        col += 1
    print("")
    Num += 1