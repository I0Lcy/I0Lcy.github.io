xiaoming = {"name": "小明"}

# 1. 取值
print(xiaoming["name"])
# 在取值的时候，如果指定的key不存在，程序会error
# print(xiaoming["name123"])

# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming["age"] = 18  # 增加
# 如果key存在，会修改已经存在的键值对
xiaoming["name"] = "小小明"  # 修改

# 3. 删除 
xiaoming.pop("name")  # 使用pop删除name这个键值对
# 如果删除的key不存在程序会报错
# xiaoming.pop("name123")


print(xiaoming)