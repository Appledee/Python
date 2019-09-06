## comments


### variables
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)

### string: you can use single or double quote in python
my_string1 = "This is a double quote string"
my_string2 = 'This is a single quote string'
print(my_string1)
print(my_string2)


### .title() displays each word in titlecase, where each word begins with a capital letter.
### .upper()
### .lower()
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


## combine strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

## Adding Whitespace to Strings with Tabs or Newlines
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

### .rstrip() To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
### .lstrip() You can also strip whitespace from the left side of a string using the lstrip() method or 
### .strip() strip whitespace from both sides at once using strip():

favorite_language = 'python '
print(favorite_language + "demo")
#favorite_language.rstrip()
print(favorite_language.rstrip() + "demo")
favorite_language = ' python '
print("pre_demo" + favorite_language + "demo")
print("pre_demo" + favorite_language.lstrip() + "demo")
print("pre_demo" + favorite_language.strip() + "demo")


### include a single quote in a string
message = "One of Python's strengths is its diverse community."
print(message)



### Numbers

### Integer 
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(2 / 3)

print(3 ** 2)
print(3 ** 3)
print( 10 ** 6)

### float number

print(0.1 + 0.1)
print(2 * 0.1)
print(.2 * 0.2)


### Avoiding Type Errors with the str() Function
### .str() str() function tells Python to represent non-string values as strings

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)











