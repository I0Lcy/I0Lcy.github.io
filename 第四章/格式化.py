# 1. 字符串变量
name = "小明"
print("我的名字叫 %s, 请多多关照! " % name)

# 2. 整数变量
zhengshu = 1
print("我的学号是 %06d" % zhengshu)

# 3. 小数
price = float("8.5")
weight = float("7.5")
money = price * weight
print("苹果单价 %.2f 元/斤, 购买了 %.2f 斤, 需要支付 %.2f 元" % (price,weight,money))

# 4. 小数
scale = 0.1
print("数据比例是 %.02f%%" % (scale * 100))