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
mixed_list = [23, 'rue de Paris', True, [33, 28, 5]]
print(mixed_list)

print('mixed_list contains', len(mixed_list), 'elements.')

# Summary:
# - Lists are ordered (each element has a fixed position)
# - Lists are iterable (possible to get their elements one by one)
# - Lists are able to store duplicated values
# - Lists are able to store different type of elements
# - A list can be created via list() function applied to an iterable object
