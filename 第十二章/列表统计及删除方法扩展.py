from typing import Counter


name_list = ["zhangsan", "lisi", "wangwu", "wangwu"]

# len(length 长度) 函数可以统计列表中元素的总数
length = len(name_list)
print("列表中包含: %d 个元素" % length)

# count 方法可以统计列表中某一个数据出现的次数
counter = name_list.count("wangwu")
print("zhangsan出现了: %d 次" % counter)
