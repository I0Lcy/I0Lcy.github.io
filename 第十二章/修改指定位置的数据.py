name_list = ["zhangsan", "lisi", "wangwu"]
# 1. 取值和取索引
print(name_list[0])

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法，如果传递的数据不在列表中，程序会报错,如下：
# print(name_list.index["lisi123"]) 错
print(name_list.index("lisi"))

# 2.  修改
# 大白话讲就是：
# 如果要修改列表中的值，只需要写上变量然后跟上一个中括号，
# 在中括号中写上要修改的值的索引，然后在等号后面跟上要修改的内容就行了
# 列表指定的索引超出范围，程序会报错
name_list[1] = "李四"

# 3. 增加

# 4. 删除
print(name_list)