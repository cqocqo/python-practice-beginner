# Conventionally, tuples look like this  #tupes use () and lists use []
Fruit = ('apples', 4, 'bananas', 5, 'oranges', 6)
print(type(Fruit))

List_of_Fruit = ['apples', 4, 'bananas', 5, 'oranges', 6]

# We can modify elements within a list # We can't modify elements within a tuple!
List_of_Fruit[0] = 'strawberries'
print(List_of_Fruit)

# We can perform similar operations on tuples like we can with list
# slicing tuples
print(Fruit[0:3])

# recalling elements within a tuple
print(Fruit[0])

# concatenation of tuples
Fruit = Fruit[0:4] + ('cherries', 10)
print(Fruit)

# Tuples with one element must have a comma
x = (5, )
print(type(x))

# creating a tuple must have double brackets
another_tuple = tuple(('hello', 18, True))

# converting a tuple to a list and then back to a tuple
Fruit = list(Fruit)
print(type(Fruit))
Fruit.append('pears')
Fruit = tuple(Fruit)
print(Fruit)

# unpacking tuples
Fruit = ('apples', 'bananas', 'pears', 'oranges', 'strawberries')
(one, two, three, four, five) = Fruit
print(one)
print(two)

# Incorporate loops within tuples
for i in range(len(Fruit)):
    print(Fruit[i])
