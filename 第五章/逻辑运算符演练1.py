# 定义一个证书变量 age ，编写代码判断年龄是否正确
# and 运算符增强版(判断年龄)
Nianling = int(input("请输入您的年龄，注意不能超过120(0-120之间):"))

if Nianling > 0 and Nianling < 120:  # 用户输入年龄 大于0 和 (and)年龄小于120 同时成立则年龄正确
    print("年龄正确")
else:
    print("年龄错误") 