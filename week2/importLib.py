# Brings entire library and needs to access methods using "library_name.method()"
'''
import math
import random
import calendar 

print(math.log(10))
print(math.sin(90))
print(math.sqrt(16))
print(math.factorial(5))

print(random.random())

# different ways to import a library
print(calendar.month(2021, 7))
print(calendar.calendar(2021))
'''
# bring everything from library don't have to use library_name.method(), we can just use method()

'''
from calendar import *
print(calendar(2021))
'''

# import only the required method from library. Note:  most ideal way if only one or two features from a library
'''
from calendar import month, calendar
print(month(2025, 10))
print(calendar(2025))
'''

# importing library and storing in a variable wriiten after "as" keyword
'''
import calendar as c
from calendar import month as m
print(c.month(2025, 12))
print(m(2025, 1))
'''