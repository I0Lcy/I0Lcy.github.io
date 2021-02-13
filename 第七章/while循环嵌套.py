# while 嵌套就是：while 里面还有个 while

# 下面是我自己猜测并写的
NumberNewOne = 1

while NumberNewOne <= 10:
    print(NumberNewOne)
    NumberNewOne += 1

    while NumberNewOne <= 5:
        print("NumberNewOne小于等于5: %d" % NumberNewOne)
        NumberNewOne += 1
        continue
