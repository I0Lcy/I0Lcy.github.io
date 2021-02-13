name = "小明"


# 在使用def定义函数的时候，解释器知道下方定义了一个函数
def say_hello():

    print("hello 1")
    print("hello 1")
    print("hello 1")

print(name)

# 只有在程序中，主动调用函数，才会让函数执行
say_hello()

print(name)