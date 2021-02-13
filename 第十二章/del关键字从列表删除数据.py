name_list = ["zhangsan", "lisi", "wangwu"]

# (知道)使用 del 关键字(delete)删除列表元素
# 在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[0]

print(name_list)

# del 关键字本质上是用将一个变量从内存中删除的
name = "xiaoming"
# 如果使用 del 关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了

del name