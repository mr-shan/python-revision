import math
# string operators

fname = "Shantanu"
lname = "Kulkarni"
fullname = fname + " " + lname

# concat two string
print(fname + " " + lname)

# multiply strings bu a number(only)
print(fname * 2)

# 'in' check if a substring is a part of main string
print(fname in fullname)    # True
print("Shantanu" in fullname)    # True
print("Alex" in fullname)     # False
print("arn" in fullname)
print("SHANTANU" in fullname)   # False, case sensitive

# string replacement fields
print("My first name is {0} and last name is {1}".format(fname, lname))

# is replacement field is not found, it's treated as 'undefined'
print("My first name is {0} and last name is {1}".format(fname))

# the order of fields in format is important
print("My first name is {1} and last name is {0}".format(lname, fname))

print("")

# f strings: anything inside curly braces is executed. supported by python 3.6+
# print(f"This is fstring, name is {fname}, age is {2022 - 1980}")

# String formatting
print("Square of four is {0:6} END".format(4**2))  # right alignment (default)
print("Square of four is {0:<6} END".format(4**2))  # right alignment
print("Square of four is {0:>6} END".format(4**2))  # left alignment
print("Square of four is {0:^6} END".format(4**2))  # center alignment

print("")

# floating point precision
print("The value of PI is {0}".format(math.pi))
print("The value of PI is {0:5.2f}END".format(math.pi))   #5 is length, .2f is decimal precision
print("The value of PI is {}".format(math.pi))    #field numbers are optional
print("The value of PI is {:.2}".format(math.pi))    #f is also optional

# string interpolation (python 2 feature, depricated in new versions)
print("I am %s %s and I'm %d years old and my height is %f"%(fname, lname, 30, 5.4))

print("")

# conversions in datatypes
# str, int, float, complex, (primitive types)
print(str(1.22))
print(int("2"))
print(float("2.1233"))
print(complex(123))
print(bool(0), bool(1), bool(""), bool(0.1), bool('false'))
