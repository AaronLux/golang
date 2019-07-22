names = ["aaron", "john", "christine", "maggie","dopa","faker"]

for name in names:
    print("I love " + name.title())

# 同其他语言一样，左开右闭
for value in range(1,10,2):
    print(value)

numbers = list(range(1,10))
print(numbers)

numbers = []
for value in range(1,40):
    numbers.append(value**2)
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

# list = [vOp for v in range()]
squares = [value**2+100 for value in range(1,10)]
print(squares)