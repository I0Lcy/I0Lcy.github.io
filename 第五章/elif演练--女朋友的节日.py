# 定义 holiday_name 字符串变量记录节日名称
# 如果是情人节 应该 买玫瑰/看电影
# 如果是平安夜 应该 买苹果/吃大餐
# 如果是生日 应该 买蛋糕
# 其他的日子每天都是节日啊

holiday_name = input("请输入节日名称(情人节/平安夜/生日/其他):")

if holiday_name == "情人节":
    print("买玫瑰，看电影")
elif holiday_name ==  "平安夜":
    print("买苹果，吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("跟女朋友在一起每天都是节日啊....")