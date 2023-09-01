my_list = list(range(0, 51, 5))

print(my_list)
print(type(my_list))

# Operations on lists:
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# This returns the 6th element in the list (where we begin at the 0th element)
print(my_list2[6])
# This returns the last element in the list
print(my_list2[-1])

# Let's create a slice from 2nd element to the 4th element
print(my_list2[4:10])

# Length of a list
print(len(my_list2))

# Maximum and minimum of a list
print(max(my_list2))
print(min(my_list2))

# Add an element onto our list
my_list2.append(11)
print(my_list2)

# Reverse a list
my_list2.reverse()
print(my_list2)

# Practice
this_list = ['tony', 'steve', 'thor']
# print(this_list)

this_list.append('bruce')
print(this_list)

this_list.reverse()
print(this_list)

print(len(this_list))

print(this_list[2:4])

this_list.append('natasha')
print(this_list)

this_list.insert(1,'clint')
print(this_list)