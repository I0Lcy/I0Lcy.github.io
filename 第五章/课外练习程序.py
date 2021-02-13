# 1.

print("咣咣咣")
gender = input("请输入你的性别(男 / 女):")
if gender == "男":
    print("隔壁有人在等你")
elif gender == "女":
    age = int(input("请问你的年龄是:"))
    if age >= 25:
        print("去隔壁,隔壁有人在等你")
    else:
        length = int(input("请问你的身高:"))
        if length >= 200:
            print("快去隔壁")
        else:
            print("进来吧")
else:
    print("你没有性别?")





# 2.

num=int(input("输入一个数字："))
if num%2==0:  # 如果输入的数字可以整除2(%是取余)且没有余数
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")