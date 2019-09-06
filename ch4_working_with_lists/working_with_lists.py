
### Lets use a for loop to print out each name in a list of magicians
### watch out the indentation
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
   print(magician)


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
   print(magician.title() + ", that was a great trick!")


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
   print(magician.title() + ", that was a great trick!")
   print("I can't wait to see your next trick, " + magician.title() + ".\n")


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
   print(magician.title() + ", that was a great trick!")
   print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")


### Making Numerical Lists
###Using the range() Function

for value in range(1,5):
   print(value)



###Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(1,11):
   square = value**2
   squares.append(square)
print(squares)




squares = []
for value in range(1,11):
   squares.append(value**2) 
print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))



squares = [value**2 for value in range(1,11)]
print(squares)


### Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

### starts at the beginning of the list:
print(players[:4])


### from the third item through the last item
print(players[2:])


### if we want to output the last three players on the roster, we can use the slice
print(players[-3:])



players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:") 
for player in players[:3]:
   print(player.title())



my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)





my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli') 
friend_foods.append('ice cream')
   
print("My favorite foods are:")
print(my_foods)
    
print("\nMy friend's favorite foods are:")
print(friend_foods)



### both variables point to the same list
my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work: 
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)



### refers to values that cannot change as immutable, and an immutable list is called a tuple.

dimensions = (200, 50)
print(dimensions[0]) 
print(dimensions[1])


### dimensions = (200, 50)
### dimensions[0] = 250


dimensions = (200, 50)
for dimension in dimensions:
   print(dimension)




dimensions = (200, 50) 
print("Original dimensions:") 

for dimension in dimensions:
   print(dimension)

dimensions = (400, 100) 
print("\nModified dimensions:")

for dimension in dimensions:
   print(dimension)





















