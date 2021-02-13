# 循环的作用就是让 指定的代码 重复的执行
# while 循环最常用的应用场景就是 让执行的代码 按照 指定的次数 重复 执行
# 需求 -- 打印5遍hello-python
# 思考 -- 如果要求打印100遍呢？

# 初始变量 number 的值为 1
number = 1

while number <= 5:  # 判断初始变量的值是否小于等于5，如果成立，则循环下面的代码
    print("Hello Python")  # 每次循环输出的内容
    number = number + 1  # 每循环一次，将number的值加一次，并重新赋值给number
print("最终number的值是 %d" % number)  # %d占位，将最后变量number中的值输出

# 输出50遍hello python

NameSTrings = 1

while NameSTrings <= 49:
    print("Hello Python")
    NameSTrings = NameSTrings + 1

print("Hello Python总共输出了: %d" % NameSTrings)
