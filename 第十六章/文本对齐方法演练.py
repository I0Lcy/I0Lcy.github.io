# 文本对齐 
# 本节以下面的古诗为例子进行演练
poem = ["登鹳雀楼",
         "王之涣",
         "白日依山尽",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]

# 按照顺序输出文章内容
for i in poem:
    print(i)
print("-" * 100)
# 居中显示
for i in poem:
    print("|%s|" % i.center(10, " "))
print("-" * 100)
# 向左对其
for i in poem:
    print("|%s|" % i.ljust(10, " "))
print("-" * 100)
# 向右对其
for i in poem:
    print("|%s|" % i.rjust(10, " "))
