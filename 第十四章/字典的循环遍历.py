# 遍历 就是 依次 从 字典中获取所有键值对

xiaoming = {"name": "小明",
            "age": 18,
            "hight": 178,
            "weight": 75.5}

# 遍历ming是每一次循环中，获取到的键值对的key
for ming in xiaoming:
    print("%s - %s" % (ming,xiaoming[ming]))