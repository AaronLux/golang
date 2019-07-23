# 首字母要大写
class Dog():
    # self必须，指向自己，实例化之后运行初始化函数，类似构造函数
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.show_info_count = 0
    def sit(self):
        print("sit")
    def roll_over(self):
        print(self.name.title() + "rolled over!")
    def show_info(self):
        print(self.name.title()+ " is " + str(self.age)+ "years old. Now: "+ str(self.show_info_count) +" times.")
        # self.show_info_count+=1

my_dog= Dog("willie",12)
your_dog = Dog("puppy",8)

# <__main__.Dog object at 0x7f5b9f34c518>
# <__main__.Dog object at 0x7f5b9f34c550>
# 打印两个对象的地址
print(my_dog)
print(your_dog)

print(my_dog.name)
my_dog.show_info()
your_dog.show_info()
