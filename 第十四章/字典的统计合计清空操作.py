xiaoming = {"name": "小明", 
            "age": 18,}

# 1. 统计键值对的数量
print(len(xiaoming))

# 2. 合并字典
# 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
tmp_dict = {"height": 1.75,
            "age": 20}

xiaoming.update(tmp_dict)  # update方法可以合并字典

# 3.清空字典
xiaoming.clear()

print(xiaoming)