tple = '1', '2', '3', '4', '5'

print(tple)

print(tple[0])    # subscripting via index possible
print(tple[1])
print(tple[-1])   # negative subscripting possible
print(tple[1:3])   # slice works here

# tple[5] = 6   # immutable, does not support assignment
# tple[0] = 0   # even for existing indices
# print(tple[100])    # index out of range


mixed_tple = 'Alex', 25, 'female', '001', ['apple', 'cherry']     # mixed datatypes possible
# firstName, age = mixed_tple   # too many values to unpack

# unpacking of tuples/lists: 
# Note: The number of items in list/tuple and number of variables given must match
name, age, sex, id, fav_fruits = mixed_tple
print("{} is {} years old, a {} with id: {} likes {}".format(name, age, sex, id, fav_fruits.__str__()))


list_from_tple = list(tple)
print(list_from_tple)
print(tuple(list_from_tple))
