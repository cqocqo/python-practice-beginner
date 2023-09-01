# python types:

print(type('tony stark'))
print(type(90))
print(type(5.6))
print(type(False))

# moving to integers
print(5.6, int(5.6))  # python rounds down
print(5.6, int(5.6), int(round(5.6)))  # rounding up

# moving strings to integers
print('12345', int('12345'))

# moving to floats
print(float(18))

# moving to strings
print(str(18))
print(str(19.5))
print(type(str(19.5)))

# logical operators
# three different logical operators: 'and', 'or', 'not'

x = 6
print(x > 0 and x < 5)

y = 24
print(y % 2 == 0 or y % 3 == 0)