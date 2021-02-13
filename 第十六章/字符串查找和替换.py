# 查找字符串和替换
hello_str = "hello world"
# 1. 判断是否以指定字符串开始
# 注意：如果确实是以括号中的单词开始的，程序会返回True
# 如果不是则返回False
print(hello_str.startswith("hello"))

# 2. 判断是否以指定字符串结束
# 如果确实是以括号中的单词结尾的，程序返回True，
# 否则返回False
print(hello_str.endswith("world"))

# 3. 查找指定字符串
# 注意:index同样可以查找指定的字符串在大字符串中的索引
# index 和 find 方法的区别
# index 如果指定的字符串不存在会报错
# find 如果指定的字符串不存在，会返回-1
print(hello_str.find("w"))
print(hello_str.find("abc"))  # 不存在则返回-1

# 4. 替换字符串
# replace 方法执行完成之后会返回一个新的字符串
# 不会修改原有字符串的内容
print(hello_str.replace("world", "python"))
print(hello_str)