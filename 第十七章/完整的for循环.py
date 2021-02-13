# 在 python 中完整的 for循环 的语法如下:
# for 变量 in 集合:
#     循环体代码
# else:
#     没有通过 break 退出循环，循环结束后，会执行的代码

for num in [1,2,3]:

    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else 下方的代码就不会被执行
    print("会执行吗?")

print("循环结束")