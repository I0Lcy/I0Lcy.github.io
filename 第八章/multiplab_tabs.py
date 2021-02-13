# 转义字符调整格式
# 保持乘法表每一列的对其及格式整齐
# 学习内容1：转义字符串
#转义字符：
# \t在控制台输出一个制表符，协助文本输出文本时 保持垂直对齐
# \n在控制台输出一个换行符
# 制表符的功能是在不适用表格的情况下 在 垂直方向 按列对其文本



def multiple_table(): 

    row = 1

    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col,row,col * row), end="\t")
            col += 1
        print("")
        row += 1