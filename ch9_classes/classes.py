class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


#Any variable prefixed with self is available to every method in the class
##self.name = name takes the value stored in the parameter name and stores it
#in the variable name, 
##provide values for only the last two parameters, name and age.

### accessing attributes
my_dog = Dog('Lulu', 1.8)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


### Calling Methods
my_dog.sit()
my_dog.roll_over()



##Creating Multiple Instances
my_dog = Dog('lulu', 6)
your_dog = Dog('willie', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


#working with Classes and Instances


class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year): 
    	"""Initialize attributes to describe a car.""" 
    	self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())


###Setting a Default Value for an Attribute
class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    
    def get_descriptive_name(self):
    	"""Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        #print(long_name.title())

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()



### Modifying Attribute Values
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()


### Modifying an attributes Value through a Method
class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.""" 
        self.odometer_reading = mileage

    def get_descriptive_name(self):
    	"""Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(25) 
my_new_car.read_odometer()






class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def get_descriptive_name(self):
    	"""Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

print(0)
my_new_car = Car('audi', 'a4', 2016)
print(1)
print(my_new_car.get_descriptive_name())
print(2)
my_new_car.update_odometer(125) 
print(3)
my_new_car.read_odometer()
print(4)


##Incrementing an attributes Value through a Method


class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    
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

    def get_descriptive_name(self):
    	"""Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500) 
my_used_car.read_odometer()

## 23500 has already passed to odometer_reading
my_used_car.increment_odometer(100) 
my_used_car.read_odometer()



## Inheritance
### The __init__() Method for a Child Class



# class Car():
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 
    
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading.""" 
#         self.odometer_reading += miles

#     def get_descriptive_name(self):
#     	"""Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")



# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super(ElectricCar, self).__init__(make, model, year)
#         #super().__init__(make, model, year)

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())































































































































