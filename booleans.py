# Booleans

print(type(True))  # This type is a bool
print(type('True'))  # This type is a string

# Testing whether these statements are correct
print(5 == 5)

# Incorporating the if statement with a boolean
x = 15
y = 5
if x % y == 0:  # If x is divisible by y == remainder 0
    print(True)
else:
    print(False)

# While loop
number = 1
while number < 4:
    print(number)
    if number == 2:
        break
    number = number + 1

# Incorporating the else statement within the while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print('number is no longer less than 4')

# If statement
number = 1
if number > 0:
    print('positive number')
elif number == 0:
    print('zero')
else:
    print('negative number')