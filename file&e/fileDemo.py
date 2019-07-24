with open("../Bottle/BottleDemo.py") as f:
    # read all
    content = f.read()

print(content)
print("===============")
with open("../Bottle/BottleDemo.py") as f:
    # read all
    lines = f.readlines()
print(content)
print(len(content))
file_string =''
for line in lines:
    # print(line.rstrip())
    file_string+=line.strip()
print(file_string)
print(len(content))
