# break 和 continue 是专门在循环中使用的关键词
# break 某一条件满足时，退出循环，不再执行后续重复的代码

# break 和 continue 只针对 当前所在循环 有效

NumberStrings = 1

while NumberStrings <= 10:
    if NumberStrings == 4:  # 当Numberstings的值等于3时候(3在内)，使用break退出循环
        break
    print(NumberStrings)
    NumberStrings += 1
    