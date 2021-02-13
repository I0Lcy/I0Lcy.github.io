# 能否将函数的调用放在函数的上方？
# 不可以，应该先定义函数再调用函数

name = "小明"

# say_hello()  # 不可以，在函数还没定义的时候就调用函数会报错

# 在使用def定义函数的时候，解释器知道下方定义了一个函数

def say_hello():

    print("hello 1")
    print("hello 1")
    print("hello 1")

print(name)

# 只有在程序中，主动调用函数，才会让函数执行
say_hello()

print(name)