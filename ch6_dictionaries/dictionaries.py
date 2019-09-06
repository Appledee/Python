
### Dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


### Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)


### Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


### Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")




alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed. 
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment. 
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))



### Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5,}
print(alien_0)
del alien_0['points'] 
print(alien_0)


### A Dictionary of Similar Objects

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
print("Sarah's favorite language is " + favorite_languages['sarah'].title() +  ".")




user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
          }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


### loop all the items

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

### loop only the keys
for name in favorite_languages.keys(): 
	print(name.title())
	print(favorite_languages[name].title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +  favorite_languages[name].title() + "!")



if 'erin' not in favorite_languages.keys(): print("Erin, please take our poll!")

### Looping a dictionaries keys in order
for name in sorted(favorite_languages.keys()):
       print(name.title() + ", thank you for taking the poll.")

### .key() only return the name of a dictionary. Instead, use favorite_languages[name].title() to access its value
language = ['python', 'phil']
for value in favorite_languages.keys():
    print(value.title())
    if value in language:
        print(" Hi " + value.title() + ", I see your favorite language is " +  favorite_languages[value].title() + "!")




### Looping Through All Values in a Dictionary
### use the values() method to return a list of values without any keys.

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


### use set() to pull out the unique languages in favorite_languages.values().

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): print(language.title())


### a list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] 
for alien in aliens:
    print(alien)



# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)
# Show the first 5 aliens: 
for alien in aliens[:5]:
    print(alien)
    print("...")
# Show how many aliens have been created. yprint("Total number of aliens: " + str(len(aliens)))




# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if  alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
         alien['color'] = 'red'
         alien['speed'] = 'fast'
         alien['points'] = 15
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
    print("...")


### a list in a dictionaries
# Store information about a pizza being ordered. 
pizza = {
       'crust': 'thick',
       'toppings': ['mushrooms', 'extra cheese'],
       }
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
            "with the following toppings:")
for topping in pizza['toppings']: print("\t" + topping)



favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages: 
	    print("\t" + language.title())

### A dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}


for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())






