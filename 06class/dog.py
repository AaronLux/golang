# 首字母要大写
class Dog():
    # self必须，指向自己，实例化之后运行初始化函数，类似构造函数
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print("sit")
    def roll_over(self):
        print(self.name.title() + "rolled over!")


my_dog= Dog("willie",6)
your_dog = Dog(8,"puppy")

# <__main__.Dog object at 0x7f5b9f34c518>
# <__main__.Dog object at 0x7f5b9f34c550>
# 打印两个对象的地址
print(my_dog)
print(your_dog)

print(my_dog.name)
