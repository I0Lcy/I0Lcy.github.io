# * 运算符，不仅可以重复字符串
# 还可以将字典和元组进行重复
# * 运算符的使用范围: 字符串，元组，列表
print([1,2] * 5)
print((1,2) * 2)
# 字典不可以使用*运算符，应为字典中的key是唯一的，重复的话会出现两个相同的key，所以肯定是错的

# + 运算符，拼接
# 字符串拼接
print("hello" + "world")
# 元组拼接
print((1,2) + (3,4))
# 列表
print([1,2] + [3,4])
# + 运算符和extend方法有点像，下面看看
t_list = [1,2]
t_list.extend([3,4])
print(t_list)
# append()方法
t_list.append(0)
print(t_list)
# append()小演练
t_list.append([8,9])
print(t_list)
# append()方法和entend()方法的区别在于
# extend方法会打散传入的值，
# append方法会原封不动的将元素传递给变量