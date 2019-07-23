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

my_car = Car("BMW","Q5",2019)
my_car.show_info()

my_car.update_odometer(300)
my_car.show_info()

my_car.update_odometer(200)
my_car.show_info()

my_car.increment_odometer(500)
my_car.show_info()