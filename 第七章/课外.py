# 用户登录管理



# trycount = 0

# while trycount < 3:
#     name = input('用户名:')
#     passwd = input('密码:')
#     if name == 'root' and passwd == 'westos':
#         print('登录成功')
#         break
#     else:
#         print('登录失败')
#         print('您还剩余%d次机会' %(2 - trycount))
#         trycount += 1
# else:
#     print('登录次数超过三次，请稍后登录')


# print("-" * 100)




# 倒着输出5个星星(*)
i = 1
while i <= 5:
    j = 1
    while j <= (5 - i):
        print(" ",end='')
        j += 1  # 执行完这一小块while语句后=，j的值是5，i的值是1
    while (j > (5-i) and j <= 5):
        print("*",end='')
        j += 1
    print()
    i += 1

# 星星倒立

i = 1
while i <= 5:
    j = 1
    while j < i:
        print(" ",end='')
        j += 1
    while j >= i and j <= 5:
        print("*",end='')
        j += 1
    print()
    i += 1