# 元组的定义
# Tuple（元组）与列表类似，不同之处在于 元组不能修改

# 元组表示多个元素组成的序列
# 元组在python开发中，有特定的应用场景

# 用于存储遗传信息，数据之间使用 , 分隔
# 元组用 () 定义
# 元组的索引从0开始
# 索引 就是数据在元组中的位置编号


info_tuple = ("zhangsan", 18, 1.75)
print(type(info_tuple))
print(info_tuple[0])
print(info_tuple[1])
print(info_tuple[2])

# 创建空元组
empty_typle = ()
print(type(empty_typle))

# 元组中 只包含一个元素时，需要 在元素后面添加逗号
# 下面的程序，type会输出类型int，这是应为在至只有一个数字的时候
# python就会认为这是一个int型变量，如果在5的后面跟上逗号，
# 再次type输出，就会变成tuple(元组)类型

single_tuple = (5)
print(type(single_tuple))