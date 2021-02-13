# 函数嵌套的演练 -- 打印分割线
# 体会以下工作中 需求是多变 的

# 需求
# 1.定义一个print_line函数能够打印 * 组成的一条分割线

def print_line():
    print("*" * 50)
print_line()

# 需求
#2.定义一个函数能够打印 由任意字符串组成的分割线
def print_nue(char):
    print(char * 50)

print_nue("-")

# 需求
#3.定义一个函数能够打印 任何重复次数 的分割线
def print_mes(back, time):
    print(back * time)

print_mes("-", 40)