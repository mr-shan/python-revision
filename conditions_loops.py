numbers = range(1, 11)

print(numbers)

for num in numbers:   # start of new scope
  print("The number is {}".format(num))
  
# end of for loop, and it's scope
print("*" * 20) # new scope


random_num = 1
# random_num = int(input("Please enter a number"))

if random_num == 0:
  print("The number is zero")
elif random_num % 2 == 0:
  print("The number is even")
elif random_num % random_num == random_num:
  pass
else:
  print("The number is odd")
  
  
print(5 in numbers)
print(100 in numbers)
print(100 not in numbers)
  

while random_num != 0:
  print("The number is {}".format(random_num))
  random_num -= 1   # augmented assignment of numbers (more efficient in python)
else:
  print("The while loop was executed without any inturrption")

# else block in a while/for loop will be executed 
# if a loop won't have any break, continue or exception.
# this is more like finally block for loop
  
# more about range, range(start_value, end_value, step)
# start_value is included, end_value is not included. step is increment
print(range(-4, 5, 1))
print(range(-10, 11, 2))
print(range(5, 0, -1))

print(str(None))
