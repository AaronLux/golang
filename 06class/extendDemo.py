
class Car():
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # def get_descriptive_name(self):

    def read_odometer(self):
        print(str(self.odometer_reading)+ "miles.")

    def update_odometer(self,mileage):
        # 对参数的校验等逻辑操作可在此处
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles


    def show_info(self):
        print("My car is " + self.name.title()+self.model+" bought in "+str(self.year)+ " "+str(self.odometer_reading)+" miles.")

class ElectricCar(Car):
    def __init__(self,name,model,year):
        # TODO 注意这里的括号啊。关键字不代表超类，要函数调用啊
        super().__init__(name,model,year)
        self.battery = Battery()

    # 给子类定义属性和方法
    def show_electric_info(self):
        print("battery ....."+ str(self.battery.battery_size))

    # 重写父类方法
    def show_info(self):
        print("electric info..")

class Battery():
    def __init__(self,battery_size = 400):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")
    def get_range(self):
       # range =0
       # global range
        if self.battery_size == 70:
            range =200
        elif self.battery_size ==400:
            range = 270
        message = "This car can go approximately "+ str(range)
        message += " miles on a full charge."
        print(message)


my_e_car = ElectricCar("M", "s9", 2018)
my_e_car.show_info()
my_e_car.battery.describe_battery()
my_e_car.battery.get_range()