# Functions in python

# The general form of a python function is:
# def function_name(arguments):
#   {lines telling the function what to do to produce the result}
#   return result

# Function that returns x^2 + y^2
def squared(x, y):
    result = x**2 + y**2
    return result


print(squared(20, 2))


# new function
def born(country):
    return print('I am from' + country)


born(' England')
