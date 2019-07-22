names = ["aaron", "john", "christine", "maggie", "dopa", "faker"]
print(names[1:6])

print(names[1:6:2])

print(sorted(names)[-3:])

others_name = names
print(others_name)
names.append("testname")
print(names)
print(others_name)
print(names.count("aaron"))