# 让列表不可以被修改，以保护数据安全
# 元组和列表之间的转换

# 自写:

# 1.使用list 函数可以把元组转换成字符串
info_tuple_list = ("zhangsan", 5, 1.75)
print(type(info_tuple_list))
print(list(info_tuple_list))  # 转换成列表

# 2.使用tuple 函数可以把列表转换成元组
info_list_tuple = ["zhangsan", "wangwu", 5, 1.75]
print(type(info_list_tuple))
print(tuple(info_list_tuple))

