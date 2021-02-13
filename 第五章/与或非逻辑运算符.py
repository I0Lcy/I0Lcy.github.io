# 在程序开发中，通常在判断条件时，会需要同时判断多个条件
# 只有多个条件都满足，才能够执行后续代码，这个时候需要使用到逻辑运算符
# 逻辑运算符可以把多个条件按照逻辑进行连接，变成更复杂的条件
# python中的逻辑运算符包括：与（and）/ 或（or） / 非（not）/ 三种


# and 运算符（必须条件同时成立才返回true，有一个不成立返回False）
age = 18
file = 18
if (age and file) == 18:
    print("True")
else:
    print("False")



# or 运算符（两个条件，其中一个成立就条件就成立，两个都不成立则条件不成立，其中一个成立条件就成立）
wight = 29
bug = 19
if (wight or bug) == 20:
    print("True")
else:
    print("False")

# not 运算符（取反）
# back = 19
# hack = 19
# if (back not hack) == 19:
#     print("True")
# else:
#     print("False")