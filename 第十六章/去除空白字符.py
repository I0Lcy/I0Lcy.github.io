# 去除空白字符
space_str = " hello world "
print(space_str.lstrip())  # 删除左边的空白字符(空格)
print(space_str.rstrip())  # 删除右边的空白字符
print(space_str.strip())  # 删除左右两上的空白字符


# 例子
# 文本对齐 
# 本节以下面的古诗为例子进行演练
poem = ["\t\n登鹳雀楼",
         "王之涣",
         "白日依山尽\t\n",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]
for i in poem:
    """print函数中写入strip方法"""
    print("|%s|" % i.strip().center(10))