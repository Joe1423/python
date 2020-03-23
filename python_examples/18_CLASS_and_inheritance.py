class Car():

#constructor

    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_read = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, milage):
        if milage >= self.odometer_read:
            self.odometer_read = milage
        else:
            print('You cant rollback and odometer!')

    def increment_odometer(self, miles):
        self.odometer_read += miles

    
#When you create a child class the parent class must be part of the current file and must appear before the child class in the file. The name of the parent class must be included in the definition of the child class

class ElectricCar(Car):

    def __init__(self, make, model, year):
        #Initialize the attributes of the parent class
        super().__init__(make, model, year)
        #Initialize specific attributes for the child class
        self.battery_size = 70

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' kW/h battery')

    #To override a method from the parent class just redifine those methods in the child class

    #You can also add a class as an attribute of another


#making an instance of the class 
my_tesla = ElectricCar('Tesla', 'Model 3', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()




    