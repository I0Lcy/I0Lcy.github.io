# 定义两个变量 python_score, c_score，编写代码判断
# 要求只要有一门成绩>60分就算合格
python_score = int(input("请输入第一门考试成绩: "))
c_score = int(input("请输入第二门考试成绩: "))

if python_score >= 60 or c_score >= 60:
    print("考试合格")
else:
    print("不合格")