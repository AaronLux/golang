names = ["aaron", "john", "christine", "maggie", "dopa", "faker"]
print(names[1])
print(names[-1])

# check 这里一样会触发IndexError: list index out of range
# print(name[10])

names[1] = "sky"
print(names)
names.append("aaron")
print(names)
# IndexError: pop index out of range
# name.pop(10)

names.pop()
print(names)
print(names.sort())
print(names)

#  在什么位置插入什么元素，不是插入什么元素在什么位置
names.insert(5, "jack")
# 当然也可以插入不同的元素
names.insert(5, 5)
print(names)

del names[5]
print(names)

# 这里应该是有个循环遍历将所有传进来的值删除
names.remove("aaron")
print(names)


