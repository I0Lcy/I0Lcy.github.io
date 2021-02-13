hello_str = "hello hello"

# 1.统计字符串长度
print(len(hello_str))

# 2. 统计某一个(子字符串)小字符串出现的次数
# 注意：如果传入一个字符串中不存在的值，程序不会报错，而是会输出0
print(hello_str.count("h"))

# 3.某一个子字符串出现的位置 
# 注意：如果使用index方法传递字符串不存在，程序error
print(hello_str.index("e"))