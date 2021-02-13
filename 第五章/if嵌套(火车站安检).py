# 需求：
# 定义布尔型变量 has_ticket 表示是否有车票
# 定义整型变量 knife_length 表示刀的长度，单位：厘米
# 首先检查是否有车票，如果有，才允许进行 安检
# 安检时，首先检查道的长度，判断刀是否超过20厘米
# 如果超过20厘米，提示刀的长度，不允许上车
# 如果不超过20厘米，安检通过
# 如果没有车票，不允许进门

# 下面是自己写的，对比黑马视频看看区别和有什么改进的地方

has_ticket = True
knife_length = input("请输入刀的长度: ")

if has_ticket == True:
    if knife_length >= str(20):

        print("您的刀长: " + knife_length + "，不允许上车")
    else:
        print("您的刀长: " + knife_length + "，可以上车")
else:
    print("抱歉，您没有车票，不允许进门")






# 黑马：
has_ticket = True
knife_length = 10

if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length > 20:
        print("您携带的刀太长了，有%d 厘米长" % knife_length)
        print("不允许上车")
    else:
        print("安检已经通过，祝您旅途愉快") 
else:
    print("请先买票")