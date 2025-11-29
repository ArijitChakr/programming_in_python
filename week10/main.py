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
## Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects, which contain both data and functions.

## It helps in:
# Modeling real-world entities,
# Making code reusable,
# Achieving modularity and flexibility,
# Avoiding repetition.

## Four Pillars of OOP: 

# Encapsulation – binding data and functions together, hiding internal details.

# Inheritance – creating new classes from existing ones.

# Polymorphism – same function name behaves differently based on context.

# Abstraction – hiding complex implementation and showing only necessary features.

"""## Class ##"""
# A class is a blueprint, template, or user-defined data type used to create objects.
class Student:
     
    def __init__(self, roll_no, name, total): #"self" represents the current object on which a method is being called. "self" allows methods to access instance variables. It refers to the current instance.
        ## Attributes
        self.roll_no = roll_no
        self.name = name
        self.total = total

    def display(self):
        print(self.roll_no, self.name, self.total)
    
    def result(self):
        if(self.total > 120):
            print("Pass")
        else:
            print("Fail")

"""## Object ##"""
# An object is an instance of a class.
# If a class is a blueprint, the object is the actual thing created from it.

s0 = Student(0, "Bhuvanesh", 100)
s0.display()


"""## Inheritence and method overriding ##"""
## Inheritance allows one class (child/subclass) to acquire properties and methods of another class (parent/superclass). 

# Method overriding occurs when the child class defines a method with the same name as the parent class to change its behavior.

"""## Importing from other files ##"""
from Student import Student1
from Employee import Employee

s = Student1("Rida", 20, 250, "Female")
s.display()

e = Employee("Harsh", 30, 50000, "Female")
e.display()


""" 
-: Types of inheritence :-
 simple inheritence : 1 parent class, 1 child class
 
 Hierarchical inheritence: 1 parent class, multiple child classes
 
 Multiple inhertence: Multiple parent class, single child class
 
 Multilevel Inheritence: one parent class(grandparent), 
 
 intermediate class(Parent), child class(child)
 
 Hybrid Inheritence:  any combination of the above 4 type of inheritence
"""






































