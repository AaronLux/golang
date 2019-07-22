name = "aaron"
print(name.title())
print(name.capitalize())
print(name.isdigit())
print(name.upper())
print(name.lower())

first_name = "aaron"
last_name = "anderson"
print(first_name +" "+ last_name)

message = "Hi, "+ first_name.title() + " " + last_name.title() + "!"
print(message)

#删除空白，rstrip,lstrip,strip.  注意这里的删除只是临时的
favorite_language = " go "
print(favorite_language.strip())
print(favorite_language)

favorite_language = favorite_language.strip()
print(favorite_language)
