# python内置函数

# del()：

# del的使用
a = [1,2,3]
del a[1]
print(a)
# del函数的方式删除变量a中的值
del(a[1])
print(a)
# 删除整个变量a
# 程序会报错，因为如果删除了变量a，变量a就不存在了
# del(a)
# print(a)

# len()：
b = [1,2,3]
print(len(b))

# max():
# 返回容器中最大值
t_str = "asckHDCKBDJKBKJDBDBCBDKBKJB"
print(max(t_str))

# min():  
# 返回容器中元组最小值
s_str = "asasjilxhlidsanlkvnlfdn"
print(min(s_str))

t_list = [1,2,3,4,5,6,7,8,9]
print(max(t_list))
print(min(t_list))

# 如果是字典，只针对key比较(max,min)
# 字典中键值对的大小比价

t_tuple = {"a": "z", "b": "y", "c": "x"}
print(max(t_tuple))
print(min(t_tuple))

# # 一句话概括本节内容就是：
# len()函数可以判断有多少个字符
# del()既可以当作函数使用，也可以当作关键字使用，del可以删除值
# # 注意：max()和min()如果遇到字典，就只比较key的大小，不会比较值
# max()函数可以判断最大值
# min()函数可以判断最小值