### list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

### By asking for the item at index -1, Python always returns the last item in the list:
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


### relpace/update an element in a list

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles[0] = 'ducati' 
print(motorcycles)


### Appending Elements to the End of a list
###The simplest way to add a new element to a list is to append the item to the list. 

motorcycles.append('ducati') 
print(motorcycles)


### The append() method makes it easy to build lists dynamically. 
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


###Inserting Elements into a List
### add a new element at any position in your list by using the insert() method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') 
motorcycles.insert(1, 'Toyota') 
print(motorcycles)

### removing an Item Using the del Statement

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0] 
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)


### removing an Item Using the pop() Method

### The pop() method removes the last item in a list, but it lets you work with that item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)


### Popping Items from any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(1)
print(motorcycles)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


### removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati') 
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


### Organizing a List

### sort() method makes it relatively easy to sort a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


### sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
### reverse alphabetical order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


### To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)



### Printing a List in Reverse Order
### To reverse the original order of a list, you can use the reverse() method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

### Finding the Length of a List
### find the length of a list by using the len() function.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
















