import json

username = input("What is your name?")

filename = "username.json"

# 注意这里要指定，不会默认创建
with open(filename,'w') as f:
    json.dump(username,f)
