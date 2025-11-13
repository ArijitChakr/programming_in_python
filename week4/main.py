'''## Lists ##'''

l = [1, 2, 3, 4, 5]
print(l)

#list.append(val):  adding an item to the list 
l.append(1024)
print(l)

#list.remove(val): removes an existing value from the list, if there is 2 value it removes the first occurance of the provided value
l.remove(1)
print(l)

'''## matrices ##'''

# matrices using 2 dimensional list

M = [[1,2,3],[4,5,6],[7,8,9]]

print(M)
print(M[0])
print(M[0][0])

'''## Lists and Sets ##'''

# another way of creating a list
l = list(range(10))

print(5 in l) ## in keyword with a value is used to determine if a value is available in the list , it returns boolean value


'''# Sets #'''
## A set in Python is a collection of unique, unordered elements: Set does not contain a duplicate element 
x = {1,2,3,5,6, 1}
print(x)

##set alse have access to "in" keyword

# Searching in list is a bit difficult and searching in Set is very easy
import sys

x = list(range(100))
y = set(range(100))

print(sys.getsizeof(x))
print(sys.getsizeof(y))

# Sets takes a lot more memory than a list while list take a mot less memory

# sets elements cannot be accessible by index
# When you say a collection is unordered, it means: The elements have no fixed position or index. Python doesn’t guarantee any consistent order of elements inside the set (the order can even change internally).

## Sets don’t support indexing because they are unordered, and indexing only makes sense for ordered collections like lists or tuples.

## When to use list or set ##
# Use list → when order and position matter.
# Use set → when uniqueness and membership checking matter.


'''###### Tuples ######'''
t = (1, 2, 3)

# A tuple in Python is an ordered, immutable (unchangeable) collection of elements.

# Properties
# Ordered — elements have a fixed sequence
# Immutable - You cannot change, add, or remove elements after creation
# Duplicates - Allowed
# Indexing — you can access elements using indexes
# Heterogeneous - Can contain different data types (e.g. integers, strings, floats, etc.)

# Usage of tuples: Use a tuple when the collection of items is fixed, ordered, and should not be modified.

'''## Operations with lists ##'''

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l12 = l1 + l2
l21 = l2 + l1
print(l1, l2) # using plus operator on a list maintains the order of the lists.


l1 = [0] * 5 # [0,0,0,0,0] list can be multiplied

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = [1, 3, 2]

print(l1 == l2) # We can use equality operator in lists
print(l2 < l3) # comparison operator can be used in lists, it compares the first element of the compared lists

# lists are mutable, we can change a value inside the list
l = [1, 2 , 4]
l[2] = 3
print(l)


l1 = [1, 2, 3]
l2 = l1
l1[0] = 100
print(l1, l2) # [100, 2, 3] [100, 2, 3]
'''
l1 = [1, 2, 3]
A list object [1, 2, 3] is created in memory.
l1 is a reference (or pointer) to that list.

l2 = l1
This does not create a new list.
It simply makes l2 point to the same list object that l1 refers to.
Now both l1 and l2 refer to the same memory location.

l1[0] = 100
You are modifying the first element inside that shared list.
Since both l1 and l2 point to the same object, the change is visible through both.

print(l1, l2)
Both show [100, 2, 3], because there’s actually just one list in memory.
'''

l1 = [1, 2, 3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()
l5 = l1

l2[0] = 100
l3[1] = 200
l4[2] = 300

print(l1, l2, l3, l4)
#It has no effect because the above lists are not using a single memory location.

print(l1 is l2, l1 is l3, l1 is l4, l1 is l5)
# using 'is' operator we can get boolean value if 2 lists are sharing same memory location or not

def add(x):
    x.append(1)
    return x

x = [5]
print(add(x)) # [5, 1]
print(x) # [5, 1]

# When you pass a variable to a function, Python passes the reference to the object, not the actual object itself — but the reference is passed by value.

# If the function argument is of mutable type then it is "Call by reference", otherwise it is "call by value"(for immutable type function argument)

## Methods of lists ##
l = [1, 2, 3]
x = l.copy() # list.copy(): copies the list and creates a same list assigned to the mentioned variable.
print(x, l) 

l.insert(2, 9) # list.insert(index, value) : similer to append but adds the mentioned value at the mentioned index in the list.

l.pop(0) # list.pop(index) : similer to remove method, but removes the mentioned index value from the list whereas, list.remove(val) removes the mentioned value from the list.

y = [2, 6, 1, 50, 3, 7, 5]
y.sort() # list.sort(): sort a list in ascending order by default
y.sort(reverse= True) # reversed = True argument in the sort function sorts a list in descending order.

x = [1, 2, 3]
x.reverse() # list.reverse(): reverse the entire list like 1st element becomes the last element and vice versa.

''' ## Operations with Sets ##'''

st = {1, 2, 3, 4, 5}
# Set does not allow duplicate values, it's an unordered entity
# Python set has same methods like mathematics for sets
A = {1, 3, 5}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))
print(A.issuperset(B))

# Union
u1 = A.union(B)
u2 = A | B
print(u1, u2)

# Intersection
I1 = A.intersection(B)
I2 = A & B
print(I1, I2)

# set difference
D1 = A.difference(B)
D2 = A - B
print(D1, D2)


'''## Operations to Tuples ##'''

# Tuples are immutable, so once a tuple is created we cannot change values inside a Tuple

# while tuples may not be used while writing python code, however tuples are majorly used for packing and unpacking by python.

#Packing
t = 1, 2, 3
print(t, type(t))
#unpacking
x, y, z = t
print(x, y, z)

# While assigning multiple values to multiple variable using assignment operator, python does packing the right hand side values into tuples and unpacking in the left hand side variables
x = 5
y = 10
x, y = y, x
print(x, y)

# Whenever we create a tuple using '()' and insert only a single value, python does not consider it as a tuple instead consider it as a single value. Therefore in order to create a tuple with single value we need to mention (val,), then python considers it as a tuple
t1 = (10)
print(t1, type(t))
t2 = (10,)
print(t2, type(t2))

# Tuple does not allow us to change any value of it's object, however if we create a tuple with lists, we cannot change/update the entire list, however we can change values inside that lists
# In python programming this is called 'Hashable'
t3 = ([1, 2], ['a', 'b'])
# t3[0] = 10 (gives error)
t3[0][0] = 10 # values inside a list which is a tuple object can be changed  
print(t3)

#hashable : If values inside a tuple are immutable , then the tuple is called as hashable
th = (1, 2, 3)
#Non-hashable: If values inside a tuple are mutable , then the tuple is called as hashable
Tnh = ([1, 2, 3],)


'''## Functional programming ##'''
# reduces number of lines instead of the normal syntax

a = 10
b = 20
#if-else
'''
if a < b:
    small = a
else:
    small = b
'''
small = a if a < b else b
print(small)

# while loop
x = 5
while a > 0: print(a); a -= 1

## List comprehension ##

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

'''
newList = []
for fruit in fruits:
    if 'n' in fruit:
        newList.append(fruit.capitalize())
print(newList)
'''
newList = [fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newList)
