# # 随机数的处理
# # 在python中，要使用随机数，首先需要导入 随机数 的 模块 -- "工具包"
# # 使用 import random 导入
# 导入模块后，可以直接在 模块名称 后面敲一个 . 然后按Tab键，会提示该模块中包含的所有函数

# 使用：

# random.randint(a,b) 返回 [a , b] 之间的整数，包含 a , b
# 例如：
# random.randint(12, 20) // 生成的随机数n: 12 <= n <= 20
# random.randint(20, 20) // 结果永远是20
# random.randint(20, 10) // 该语句是错误的，下限必须是小于上限

