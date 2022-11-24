# functions

def addition(num1, num2):
  """
  adds two numbers
  :param num1: first number
  :param num2: second number
  :return: addition of `num1` and `num2`
  """
  return num1 + num2
  
  
def division(num1, num2 = 1):
  """
  A default value is given to argument num2
  """
  return num1 // num2
  
  
def add_numbers(*args):
  """
  accepts variable number of arguments.
  all args are clubbed in a tuple.
  Here args is a tuple
  """
  sum = 0
  for num in args:
    sum += num
  
  return sum
  
  
# # argument types: The default order for argument is given below
# def func(p1, p2, *args, k, **kwargs):
#   print("positional or keywords: {}, {}".format(p1, p2))
#   print("var-positioned: {}".format(args))
#   print("keyword: {}".format(k))
#   print("var-keyword: {}".format(kwargs))
  

print(addition(1, 2))   # positional arguments
print(addition(num2=100, num1=200))   # keyword arguments

print(add_numbers(1, 2, 3, 4))

print(division(4))
