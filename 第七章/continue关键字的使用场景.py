# break 和 continue 是专门在循环中使用的关键词
# break 某一条件满足时，退出循环，不再执行后续重复的代码

# break 和 continue 只针对 当前所在循环 有效

NumberNewOne = 1

while NumberNewOne <= 10:
    if NumberNewOne == 5:  # 注意在循环中，如果使用 continue 这个关键词
        NumberNewOne += 1
        continue           # 在使用关键字之前，需亚确认循环的计数是否修改，否则可能会导致死循环
    print(NumberNewOne)
    NumberNewOne += 1