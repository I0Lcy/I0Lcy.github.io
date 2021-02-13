name_list = ["zhangsan", "lisi", "wangwu"]
num_list = [6, 8, 4, 1, 10]

# 升序
name_list.sort()
num_list.sort()

# 降序
name_list.sort(reverse=True)  # reverse=True 触发反转条件
num_list.sort(reverse=True)

# 逆序 (反转)
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)