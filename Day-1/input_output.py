# input() is used to take user input from the keyboard.
# print() is used to show output on the screen.

# Taking input from user (input returns string)
name = input("Enter your name: ")
age = input("Enter your age: ")

# You can use int() to convert age to a number if needed
# age = int(input("Enter your age: "))  # Uncomment to convert to number

# Displaying a personalized message
print("Hello", name + "!")  # Using + to join strings
print("You are " + age + " years old.")  # Age is treated as string here

# Using f-string for cleaner formatting (recommended)
print(f"Nice to meet you, {name}. You are {age} years old.")

# Using end to print in oneline (no newline will be used)
print("Hello",name,end=" ")
print("You are",age," years old",end=" ")
