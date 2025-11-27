"""## Exception handling ##"""
'''
try:
    # risky code
except ExceptionType1:
    # handle exception 1
except ExceptionType2:
    # handle exception 2
else:
    # executes if no exception
finally:
    # executes always

Common exceptions:
    ZeroDivisionError
    ValueError
    IndexError
    TypeError
    FileNotFoundError
'''

a = 20
b = 0

try:
    c = a/b
    print(c)
    f = open("abc.txt", "r")
except ZeroDivisionError:
    print("Invalid Input, divisor cannot be 0")
except NameError:
    print("variable not defined")
except FileNotFoundError:
    print("File not found in directory")
except: # for any error other than common errors
    print("Something went wrong")
finally:
    f.close()
## Raising Your Own Exception

def check_age(age):
    if age < 0:
        #raise ValueError("Age cannot be negative")
        raise Exception("underage")
    

"""## Obejct Oriented Programming(OOPs) ##"""

































