# 用嵌套打印小星星

# 需求：
# 在控制台连续输出五行 * ，每一行星号的数量依次叠加


# 我写的垃圾的代码：
Number = 1

while Number <= 1:
    print("*")
    Number += 1
    while Number <= 2:
        print("**")
        Number += 1
        while Number <= 3:
            print("***")
            Number += 1
            while Number <= 4:
                print("****")
                Number += 1
                while Number <= 5:
                    print("*****")
                    Number += 1
print("-" * 50)

# 黑马写的
# 开发步骤:
# 1>完成5行内容的简单输出
# 2>分析每行内部的*应该如何处理?

row = 1
# 每一行要打印的星星就是和当前的行数,是一致的
while row <= 5:
    col = 1  # 定义一个列变量
    while col <= row:  # 增加一个小的循环，专门负责当前行中，每一行 '列' 的星星的显示
        # print("%d" % col)
        print("*", end="")
        col += 1
    print("")
    row += 1
print("+" * 100)

# 换一个我能看懂的注释

row = 1  # 初始变量1（行变量）

while row <= 5:  # 如果初始变量row的值小于等于5，执行下方代码块
    col = 1  # 定义一个列的变量（列变量）
    while col <= row:  # 如果列变量的值小于等于row，执行下方代码块
        # print("%d" % col)
        print("*", end="")  # 输出一个星号，并使用end=""方法，将打印出来竖着的星号仅仅排列起来
        col += 1  # col（列变量）的值加一
    print("")  # 这里不可以省略
    row += 1

    
row = 1

while row <= 5: 
    col = 1
    while col <= row:
        print("*", end="") 
        col += 1
    print("")
    row += 1
