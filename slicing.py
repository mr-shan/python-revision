fullname = "Shantanu Kulkarni"

print(fullname[0:9])    #first name: start index included. end index character not
print(fullname[:9])    #start index is optional. defaults to start of string
print(fullname[9:])     #last name: end index is optional, defaults to end of string

# negative indexing
# both the index can be negative
# start should always be lesser than end index
print(fullname[-8:])  #start index -8 means reverse order from end, end is optional
print(fullname[-17:-8])   #end index should be greater than start index


print(fullname[0:10000])  #end index can go out of range


# step in the slicing
# step is incremental value for index, it can't be zero(value error exception)
print(fullname[0:9:1])  #index is incremented by 1
print(fullname[0:9:2])  #index is incremented by 2


# negative steps
# start index must be greater than end index
print(fullname[9:0:-1]) #start at 9, end at 0 go reverse as step is -ve
print(fullname[::-1])   #reverse whole string

print("")

# common python idioms:
print(fullname[::-1])   #reverse the sequence

# these two are safer than subscripting the sequence.
# e.g. fullname[0] or fullname[len(fullname) - 1]
# they handles the array range exception
print(fullname[-1:])    #last item in the sequence
print(fullname[:1])     #first item in the sequence
