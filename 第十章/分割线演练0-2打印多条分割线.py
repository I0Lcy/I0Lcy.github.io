# 需求：
# 定义一个函数能够打印五行分割线，分割线要求需要满足上一届第三个需求

def print_line(char, times):
    
    print(char * times)

def print_lines():
    row = 0
    while row <= 5:
        print_line("-", 50)
        row += 1
print_lines()