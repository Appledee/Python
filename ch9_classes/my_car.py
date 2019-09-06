### import class

#from car import Car, ElectricCar
#import car
from car import *
from collections import OrderedDict


my_new_car = Car('audi', 'a4', 2019)
#my_new_car = car.Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 33
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
#my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


my_beetle = Car('volkswagen', 'beetle', 2016)
#my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
#my_tesla = ElectricCar('tesla', 'roadster', 2016) 
print(my_tesla.get_descriptive_name())



favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python' 
favorite_languages['sarah'] = 'c' 
favorite_languages['edward'] = 'ruby' 
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items(): 
	print(name.title() + "'s favorite language is " +
           language.title() + ".")














