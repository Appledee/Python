### functions

def greet_user():
   """Display a simple greeting."""
   print("Hello!") 
greet_user()


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')


def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Specify default type

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')



### These are all equivalent
  # A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
   # A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')



### return a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted.""" 
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)



def get_formatted_name(first_name, middle_name, last_name):
       """Return a full name, neatly formatted."""
       full_name = first_name + ' ' + middle_name + ' ' + last_name
       return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)



### Making an argument optional 
def get_formatted_name(first_name, last_name, middle_name=''): 
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
   
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)


### Return a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


### return a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
       person['age'] = age
    return person
   
musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# ### Using a function with a while loop

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#    # This is an infinite loop!

# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")




# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

# formatted_name = get_formatted_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")



# Please tell me your name: (enter 'q' at any time to quit) First name: eric
# Last name: matthes
# Hello, Eric Matthes!
# Please tell me your name: (enter 'q' at any time to quit) First name: q



### Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)



### Modifying a List in a Function

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    # Display all completed models.

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)



def print_models(unprinted_designs, completed_models): 
    """ Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed.""" 
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
        print(completed_model)
   

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)
# print(completed_models)



### Preventing a Function from Modifying a List
##The slice notation [:] makes a copy of the list to send to the function. 
#If we didnt want to empty the list of unprinted designs
##we could call print_models() like this:

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)




### Passing an arbitrary number of arguments

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')




### Mixing Positional and Arbitrary Arguments

#If you want a function to accept several different kinds of arguments, 
#the parameter that accepts an arbitrary number of arguments must be placed last 
#in the function definition. 
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) +
#           "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')




### Using Arbitrary Keyword Arguments
### The function would work no matter how many additional key-value pairs are provided in the function call.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics',
                             contribution = 'great'
                             )
print(user_profile)



### storing your functions in modules

### save this file in pizza.py
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) +
#     "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)


# we ll make a separate file called making_pizzas.py in the same directory as pizza.pydirectory as pizza.py..
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# module_name.py

#import module_name
#module_name.function_name()


## from module_name import function_name

## from module_name import function_0, function_1, function_2

from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')





#Using as to Give a Function an Alias
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


### from module_name import function_name as fn


### Using as to Give a Module an Alias
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

### import module_name as mn


### Importing All Functions in a Module. Wildcard import
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

### from module_name import *



### 
#If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:

#def function_name(parameter_0, parameter_1='default value')

## The same convention should be used for keyword arguments in func-tion calls:

#function_name(value_0, parameter_1='value')



# def function_name(
#                 parameter_0, parameter_1, parameter_2, parameter_3, 
#                 parameter_4, parameter_5):
#     function body...

























