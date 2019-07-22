favorite_language = {
    "aaron":"go",
    "dopa":"java",
    "faker":"c",
    "the_shy":"php",
    "maggie":"go"
}

for key,value in favorite_language.items():
    print(key.title() + " love ",value.title()+"!")

# 使其有意义，这个可以。。
for name,language in favorite_language.items():
    print(name.title() + " love ",language.title()+"!")

#遍历所有的键
for name in favorite_language.keys():
    print(name)

#顺序遍历
for name in sorted(favorite_language.keys()):
    print(name)

# 这里不能用sort，改变一个字典没意义啊！
# 同样的，遍历所有的值
for language in favorite_language.values():
    print(language)

for language in sorted(favorite_language.values()):
    print(language)

print("The following language have been mentioned:")
for language in set(favorite_language.values()):
    print(language)