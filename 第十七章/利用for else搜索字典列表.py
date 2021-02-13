# 应用场景
# 在迭代遍历嵌套的数类型时，例如 一个列表包含了多个字典
# 需求：要判断 某一个字典中是否存在 指定的 值
# 如果 存在，提示并且退出循环
# 如果不存在，在循环整体结束后，希望得到哦一个统一的提示

students = [
    {"name": "阿土",
    "age": 20,
    "gender": True,
    "height": 1.7,
    "weight": 75.0},
    {"name": "小美",
    "age": 19,
    "gender": False,
    "height": 1.6,
    "weight": 45.0},
]

find_name = "阿土"
for haha in students:
    print(haha)
    if haha["name"] == find_name:
        print("找到了 %s" % find_name)
        break
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望得到一个统一的提示！
    print("抱歉，没有找到 %s" % find_name)
print("循环结束")
