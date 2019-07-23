class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        print(self.age)

    def update_age(self,age):
        last_age = self.age
        self.age=age
        print("update age from "+ str(last_age)+ " to "+ str(age))

    def show_info(self):
        print(self.name + " is "+ str(self.age) + " years old." )


