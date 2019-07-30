# dict in list
person1 = {"name":"aaron","age":18}
person2 = {"name":"dopa","age":19}
person3 = {"name":"maggie","age":18}
person4 = {"name":"faker","age":28}
person5 = {"name":"john","age":66}
person6 = {"name":"jack","age":118}

employee = [person1,person2,person3,person4,person5,person6]

for person in employee:
    print(person)

employee = []
for person in range(30):
    new_guy = {"name":"some names","age":18}
    employee.append(new_guy)
print(employee[-7:])


# list in dict
person1 = {
    "name":"aaron",
    "hobbies":["reading","coding"]
}
print(person1["hobbies"][0])

for hobby in person1["hobbies"]:
    print(hobby)

# dict in dict
users = {
    "aaron":{
        "age":18,
        "job":"coding"
    },
    "maggie":{
        "age":18,
        "job":"beauty"
    }
}
print("users:")
for user_name,user_info in users.items():
    print("name: ",user_name)
    print("age: ",user_info["age"])
    print("job: ",user_info["job"])