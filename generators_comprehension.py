import sys

def my_range(num: int, step: int = 1):
    counter = 0
    while counter < num:
        yield counter
        counter += step


def fibonacci():
    current, next = 1, 0
    while True:
        yield next
        current, next = current + next, current
        

string = "this is the string and made just for list comprehension. Now you can see how much difference it makes in memory. Even if I increase the size of string, the size of generator will remain same"

upper_case_words = [str.upper() for str in string.split(' ')]
print(sys.getsizeof(upper_case_words))
print(sys.getsizeof(str.upper() for str in string.split(' ')))

print(upper_case_words)
print(str.upper() for str in string.split(' '))
