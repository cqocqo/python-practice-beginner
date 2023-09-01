# Q1: Assigning variables and find the addition, division, subtraction and multiplication
x = 5   # assigned x variable equal to 5
y = 10  # assigned y variable to 10

print(x + y)  # addition
print(x/y)    # division
print(x - y)  # subtraction
print(x*y)    # multiplication

# Q2:
my_list = list(range(0, 101, 2))  # Create a list of all the even numbers from 0 to 100.
print(my_list)

print(my_list[0:10])             # Then print the first 10 elements and find the length of this list.
print(len(my_list))              # Append a value of your choice to the end of this list

my_list.append(200)
print(my_list)

# Assign a variable to any integer you want and find whether this integer is divisible by 5
number = 78
if number % 5 == 0:
    print('is divisible by 5')
else:
    print('is not divisible by 5')

# Q3: Using a for loop, get python to print the numbers 0 to 5
for i in range (6):          # We use 6 because the range command takes up to the value n-1
    print(i)

# Q5: Draw a pentagon in turtle:
import turtleproject
# My answer:
# turtle.bgcolor('white')
# turtle.pensize(2)
# turtle.color('black')
# turtle.speed(10)
#
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)
# turtle.left(72)
# turtle.done()
# Better way to do it is using the 'for' loop
for i in range(5):       # Pentagon has 5 sides
    turtle.right(72)     # This is the angle needed to produce a pentagon
    turtle.forward(100)  # Will give length of the pentagon size
turtle.done()

# Q6: Create a function that tests whether three numbers (a,b,c) are a Pythagorean triple
def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


print(pythagorean_triple(3, 4, 5))
print(pythagorean_triple(3, 9, 15))

# Spot the error
# n = 5
# while n > 0
# n = n + 1
#   print(n)

# n = 5
# while n > 0:
#     n = n + 1
#     print(n)

# Create two lists (of size 5 or any size you want)
# and plot these lists against each other using matplotlib
import matplotlib.pyplot as plt

x = [5, 10, 15, 20]
y = [2, 4, 6, 8]
plt.plot(x, y, c='red', linewidth=5, label='line 1')

x2 = [10, 11, 16, 29]
y2 = [7, 10, 17, 23]
plt.plot(x2, y2, c='blue', linewidth=5, label='line 2', linestyle='dashed')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('spangles and winghead')
plt.legend()
plt.show()