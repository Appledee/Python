
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = False
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        #long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def fill_gas_tank(self):
        """Print everycar need a gas tank."""
        print("Rember to fill the gas tank before long trip.")
        #return self.gas_tank


mycar = Car('tesla', 'model s', '2019')
print(mycar.get_descriptive_name())
print(type(Car))



class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70): 
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self.range = range

    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 0
        message = ""
        if self.battery_size >= 20 and self.battery_size <= 75:
            range = 240
        elif self.battery_size > 75:
            range = 270
        else: 
            message = " Please charge the battery. "


        message += "This car can go approximately " + str(range)
        message += " miles before charge."
        print(message)


#__metaclass__ = type

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        #self.gas_tank = 'false'
        self.battery = Battery(160)


    def fill_gas_tank(self):
        """Define a fill_gas_tank method in this child class to override the same method in the paraent class"""
        #flag = not self.gas_tank
        print("Electric Car does not need a gas tank which is " + str(not self.gas_tank))
        


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

## don't forget the bracket when you call a method .fill_gas_tank(), not .fill_gas_tank. 







