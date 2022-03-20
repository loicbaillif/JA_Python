# ****** LISTS - THEORY ******

# Create a list:
dog_breeds = ['corgi', 'labrador', 'huskey', 'pitbull']
print(dog_breeds)
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Create list using list() on iterable object
list_of_chars = list('danger!')
print(list_of_chars) # ['d', 'a', 'n', 'g', 'e', 'r', '!']
# list_of_ints = list(12345) # won't work ... int is not an iterable

# It is possible to store different data types in a same list
mixed_list = [23, 'rue de Paris', True]
print(mixed_list)