with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())


### relative path on Mac, text_files is the same level folder as the execution python file folder. 
with open('text_files/pi_digits.txt') as file_object2:
    contents = file_object2.read()
    print(contents)

### absolute path on Mac
file_path = '/Users/Will/Documents/Algorithms/Python_crash_course/ch10_files_and_exceptions/pi_digits.txt'
with open(file_path) as file_object3:
	conents = file_object3.read()
	print(conents)



filename = 'pi_digits.txt'
with open(filename) as file_object: 
    for line in file_object:
        #print(line)
        print(line.rstrip())



filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() 

for line in lines:
    print(line.rstrip())



pi_string = '' 
for line in lines:
    #pi_string += line.rstrip()
     pi_string += line.strip()
print(pi_string) 
print(len(pi_string))




filename = 'pi1m.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))


# birthday = input("Enter your birthday, in the form mmddyy: ") 

# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


with open(filename, 'w') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")




#print(5/0)


try:
   print(5/0)
except ZeroDivisionError:
       print("You can't divide by zero!")



### Using Exceptions to Prevent Crash
###This program does nothing to handle errors, so asking it to divide by zero causes it to crash:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
it = 1
while it:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ") 
    if second_number == 'q':
        break
    it -= 1
    # try:
    #     answer = int(first_number) / int(second_number)
    # except ZeroDivisionError: 
    #     print("You can't divide by 0!")
    # else: print(answer)

  # answer = int(first_number) / int(second_number)
  # print(answer)

try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError: 
    print("You can't divide by 0!")
else: print(answer)




filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read() 
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


###Working with Multiple Files
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)

    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.\n")


count_words('alice.txt')


filenames = ['alice.txt', 'alice1.txt', 'alice2.txt', 'alice3.txt'] 
for filename in filenames:
    count_words(filename)



### failing silently

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
        pass

    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.\n")

filenames = ['alice.txt', 'doesnt_exist.txt', 'alice2.txt', 'alice3.txt'] 
for filename in filenames:
    count_words(filename)



### storing data
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)




filename = 'numbers.json' 
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)



username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")


filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")




##Load the username, if it has been stored previously. 
##Otherwise, prompt for the username and store it. 

filename = 'username_another.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("The file you tried to open can't be found, A new file is created")
        print("We'll remember you when you come back " + username + "!")
else:
	print("Welcome back, " + username + "!")




def greet_user():
	filename = 'username_another.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
	    username = input("What is your name? ")
	    with open(filename, 'w') as f_obj:
	        json.dump(username, f_obj)
	        print("The file you tried to open can't be found, A new file is created")
	        print("We'll remember you when you come back " + username + "!")
	else:
		print("Welcome back, " + username + "!")

greet_user()



def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username



def greet_user():
	"""Greet the user by name. """
	username = get_stored_username()
	if username:
	    print("Welcome back, " + username + "!")
	else:
		username = input("What is your name? ")
		filename = 'username_another.json'
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("The file you tried to open can't be found, A new file is created")
			print("We'll remember you when you come back " + username + "!")


greet_user()


def get_new_username():
	""" Promp for a new username"""
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("The file you tried to open can't be found, A new file is created")
		print("We'll remember you when you come back " + username + "!")
	return username



def greet_user():
	"""Greet the user by name. """
	username = get_stored_username()
	if username:
	    print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		filename = 'username_another.json'
		print("We'll remember you when you come back " + username + "!")

greet_user()




