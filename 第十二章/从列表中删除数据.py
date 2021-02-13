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
# 1. (append()方法)
# append() 方法可以向列表的末尾追加数据
name_list.append("王小二")

# 2. (insert()方法)
# insert() 方法可以在列表的指定索引位置插入数据
name_list.insert(1, "小美眉")

# 3. (extend()方法)
# extend() 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["孙悟空", "朱二哥", "沙师弟"]
name_list.extend(temp_list)


# 4. 删除
# remove() 删除
# remove() 方法可以从指定的位置删除数据
name_list.remove("wangwu")

# clear() 方法
# clear() 方法清空列表所有内容
name_list.clear()


# pop() 方法
# pop() 方法默认可以把列表中 最后一个元素删除
# pop() 方法可以指定要删除元素的索引
name_list.pop()
name_list.pop(3)

print(name_list)