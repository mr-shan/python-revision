evens = [0, 2, 4, 6, 8, ]
odds = [1, 3, 5, 7, 9]

brands = ['apple', 'logitech', 'lg', 'samsung']

# enumerate iterates through a list and returns a tuple of index and item
for (index, item) in enumerate(evens):
  print("Index {} is {}".format(index, item))

evens.sort(reverse=True)  # sort existing list

print(evens)
  
evens = sorted(evens)   # sort the list and return a new list
print(evens)


# ways to create list
nums = list("12345")    # ['1', '2', '3'...] calling list constructor
all_nums = evens + odds

all_nums_sorted = sorted(list(all_nums))

odds_copy = odds[:]   # copy list with slice operator
odds_copy.sort(reverse=True)

# even_copy = evens.copy()

# check if copy attribute exists on evens list and if it's callable
print(hasattr(evens, 'copy') and callable(getattr(evens, 'copy')))

print(odds)
print(odds_copy)

print("*" * 20)

print("The total evens are {} and odds are {}.".format(len(evens), len(odds)))

print(callable(getattr(evens, 'count')))
# print(getattr(evens, 'count'))

print(evens.count(2))

# print('lg' in brands)
# print(brands.count('lg'))

print(" | ".join(brands))   # join all elements in brands by |, a string method, list should be strings

print(" | ".join(brands).split(' | '))    # split string by given delimiter, method of string, creates a list of splitted items

print("12345".split())  # a list of single item 12345
print(list("12345"))    # a list of 5 items

print("*" * 20)

mobiles = ['iphone', 'galaxy s9', 'blackberry', 'oneplus nord']

# print(mobiles.clear())
print(mobiles.index('blackberry'))

mobiles.insert(90, 'sony walkman')
print(mobiles.pop(4))   # remove item via it's index, index out of bound if not in list
print(mobiles.remove('blackberry'))   # remove item with it's value, exception if not in list

print(mobiles.reverse())   #reverse the existing list, return nothing

print(mobiles)

