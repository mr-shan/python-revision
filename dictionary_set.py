# Dictionaries:
# ordered (post python 3.5) datastructure of key and value pairs
# keys should be hashable and immutable (string, integer, tuple made of immutables)
# values can be anything

cars = { 1: 'honda city', 2: 'hyundai venue', 3: 'maruti swift'}

# print(cars[4])    # this will introduce key error.
# safer way to retrieve things. This won't cause exception. 
# but the indexing is a lot faster
print(cars.get(4))      # if key not found, will return None

# for key in cars:
#     print(key, cars[key])

# use items() method to get tuples of keys and values
for key, value in cars.items():
    print(key, value)


# operations on Dictionaries
cars[4] = 'jeep compass'    # insert
cars[3] = 'maruti baleno'   # update
del cars[4]     # if you are sure that key exists.
compass = cars.pop(4, None)     # safer way of deleting items

print(3 in cars)    # check if key exists
print(cars)


# setdefault()
# set the value to the given key if not already exists.
# return the value if key exists.
print(cars.setdefault(4, 'jeep compass'))
print(cars.setdefault(3, 'maruti swift'))   # maruti balen since it exists
print(cars)

print()
print("*" * 10 + " End of Dictionaries " + "*" * 10)
print()


# Sets
# set is an unordered collection of items
# items should be hashable, unique (that's why access time is same and faster for each item unlike list)
# Since it's unordered, you can subscript items via their index.
# supports all set operations (union, intersection etc.)

animal_set = { 'cat', 'dog', 'monkey', 'mouse' 'horse' }
mobile_set = set(['iphone', 'samsung', 'onepuls'])

# to create an empty set, set() must be used. {} creates a dictionary
empty1 = {}
empty2 = set()
print(type(empty1), type(empty2))

print(animal_set)   # the order of insertation is not maintained

# Membership of item check in the set
print('dog' in animal_set)
print('rabbit' in animal_set)

print({*""}, {*{}}, {*[]})      # unpacking empty sequences creates an empty set

# set functions
mobile_set.add('blackberry')    # add new item, ignore if exists
mobile_set.add('iphone')
print(mobile_set)
print(sorted(mobile_set))   # returns sorted list 
print(mobile_set.pop())     # randomly pop any item from set
