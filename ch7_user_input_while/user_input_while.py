# ### input output

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")


# >>> message = input("Tell me something, and I will repeat it back to you: ")
# Tell me something, and I will repeat it back to you: willim
# >>> print(message)
# willim


# >>> name = input("Please enter your name: ")
# Please enter your name: william
# >>> print("Hello, " + name + "!")
# Hello, william!


# >>> prompt = "If you tell us who you are, we can personalize the messages you see."
# >>> prompt += "\nWhat is your first name? "
# >>> name = input(prompt)
# If you tell us who you are, we can personalize the messages you see.
# r first name? william
# >>> print("\nHello, " + name + "!")

# Hello, william!
# >>> 


# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age
# '21'
# >>> 



# >>> age = input("How old are you? ")
# How old are you? 21 
# >>> age = int(age)
# >>> age >= 18 True




# >>> height = input("How tall are you, in inches? ")
# How tall are you, in inches? 71
# >>> height = int(height)
# >>> if height >= 36: print("\nYou're tall enough to ride!")
# ... else: print("\nYou'll be able to ride when you're a little older.")
# ... 

# You're tall enough to ride!
# >>> 



# >>> number = input("Enter a number, and I'll tell you if it's even or odd: ")
# Enter a number, and I'll tell you if it's even or odd: 21
# >>> number = int(number)
# >>> if number % 2 == 0: print("\nThe number " + str(number) + " is even.")
# ... else: print("\nThe number " + str(number) + " is odd.")
# ... 

# The number 21 is odd.



# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1



# prompt = "\nTell me something, and I will repeat it back to you:" 
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)




# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello again.
# Hello again.
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit
# quit



# prompt = "\nTell me something, and I will repeat it back to you:"
#    prompt += "\nEnter 'quit' to end the program. "
#    message = ""
#    while message != 'quit':
#        message = input(prompt)
#        if message != 'quit':
#            print(message)

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello everyone! 
# Hello everyone!
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello again.
# Hello again.
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit



# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True 
# while active:
#     message = input(prompt)
#     if message == 'quit': 
#     	active = False
#     else: print(message)


# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")


# If the modulo is 0 (which means current_number is divisible by 2), 
# the continue statement tells Python to ignore the rest of the loop and return to the beginning.

# current_number = 0
# while current_number < 10:
# 	current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)




x= 1
while x <= 5:
       print(x)
       x += 1



# Start with users that need to be verified,
# and an empty list to hold confirmed users. 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users. 
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title()) 
    confirmed_users.append(current_user)
 # Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


responses = {}
   # Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
       # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
       # Store the response in the dictionary:
    responses[name] = response
       # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
   # Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")



# What is your name? Eric
# Which mountain would you like to climb someday? Denali 
# Would you like to let another person respond? (yes/ no) yes
# What is your name? Lynn
# Which mountain would you like to climb someday? Devil's Thumb 
# Would you like to let another person respond? (yes/ no) no
             
#  --- Poll Results ---
# Lynn would like to climb Devil's Thumb.
# Eric would like to climb Denali.






























