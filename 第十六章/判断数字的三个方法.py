# 本节使用如下方法

# isdecimal()
# isdigit()
# isnumberic()

# 判断字符串中是否只包含数字
space_str = "     \t\n\r"
print(space_str.isspace)

# 判断字符串中是否包含数字
# 1> 都不能判断小数,如果是小数，则全部返回False
# num_str = "1.1"  # False
# unicode 字符串(1)
# num_str = "\u00b2"
# 中文数字
num_str = "一千零一夜"

print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())