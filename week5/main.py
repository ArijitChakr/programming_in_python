'''## Dictionaries ##'''

## A dictionary is defined using curly braces {} with key–value pairs separated by colons : .Each key in a dictionary must be unique, hashable and immutable (like strings, numbers, or tuples), while the values can be of any data type.

d = {} #if only curly brackets is used to define a variable it becomes a dictionary

student = {
    "name": "Arijit",
    "age": 21,
    "course": "Data Science"
}
print(student)
print(student["name"])

student["age"] = 22    # modify
student["grade"] = "A" # add new key-value
del student["age"]     # delete key-value pair
print(student)

print(student.keys()) # returns keys of the dictionary as a list
print(student.values()) # returns values of the dictionary as a list
print(student.items()) # returns key and value of a dictionary as a list of tuples : [('key', 'value')]


'''## Iterators ##'''
## An iterator is an object in Python that allows you to traverse (iterate over) elements one at a time.It is used in loops like for loops, list comprehensions, generators, etc.

## An iterator is an object that implements two methods:
# __iter__() → returns the iterator object itself
# __next__() → returns the next element from a sequence
# If no more items are left, it raises StopIteration.

## Key Properties ##

## 1. Iterators are Lazy: They produce items one at a time, only when requested using next(). They don’t store the whole collection in memory.

## 2. They Maintain State: An iterator remembers where it is during iteration.Once exhausted, it cannot be reset unless you create a new iterator.

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

basket = iter(fruits)

print(next(basket))
print(next(basket))
print(next(basket))
print(next(basket))
print(next(basket))
print(next(basket))

## generator: is used to create our own iterator

# yield is used inside a function to turn it into a generator.

# A generator is like a special type of iterator that produces values one at a time, only when needed.

# yield pauses the function and returns a value, but remembers where it left off, so the next call continues from the same point.

def sqare(limit):
    x = 0
    while x < limit:
        yield x * x
        yield x * x * x
        x += 1

a = sqare(5) # sqare generates an iterator and in this case a is an iterator
print(next(a), next(a))
print(next(a), next(a))

""" Lambda function """
# A lambda function in Python is a small, anonymous (nameless) function defined using the keyword lambda instead of def. It is used when you need a short, one-line function for a short time.

## properties

# It can have any number of arguments
# It must contain exactly one expression
# It automatically returns the value of that expression (no return keyword needed)

add = lambda x, y : x + y
print(add(10,20))


""" enumerate function """
# enumerate() is a built-in Python function that adds a counter (index) to an iterable.
# Syntax:  enumerate(iterable, start=0)
# Returns an enumerate object, which produces pairs of: (index, value) for each item in the iterable.

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]



for fruit in enumerate(fruits):
    print(fruit)

""" zip function """
# zip() is a Python built-in function that combines multiple iterables element-wise into tuples.
# Returns an iterator of tuples, where each tuple contains the elements from the input iterables at the same position., can be used to create dictionaries as well

size = [5, 5, 6, 6, 9, 10, 5, 4]

print(list(zip(fruits, size)))
print(dict(zip(fruits, size)))

# without using zip function

def combine_2list_of_same_length_to_list_of_tuples(l1: list, l2: list) -> list :
    new_list = []

    for i in range(len(l1)):
        new_list.append((l1[i], l2[i]))

    return new_list

comb = combine_2list_of_same_length_to_list_of_tuples(fruits, size)
print(comb)

def combine_2list_of_same_length_to_dictionary(l1: list, l2: list) -> dict :
    new_dict = {}

    for i in range(len(l1)):
        new_dict[l1[i]] = l2[i]

    return new_dict

comb_dict = combine_2list_of_same_length_to_dictionary(fruits, size)
print(comb_dict)

""" map function """

## map() is a built-in Python function that applies a given function to every item of an iterable (like list, tuple, string) and returns a map object (an iterator) that yields the results one by one.

# map(function, iterable1, iterable2, ...)

# How It Works: Takes a function > Applies it to each element(s) of the provided iterable(s) > Produces the transformed values lazily (one at a time)

a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30]

def sub(x, y):
    return x - y

c = map(sub, a, b)
print(list(c))


""" Filter function """
# filter() is a built-in Python function that filters elements from an iterable based on a condition.
# filter(function, iterable): Returns a filter object (iterator) containing only the elements for which the function returns True.

## How It Works

# The function you pass must return True or False
# filter() keeps only those items where the function returns True
# Results are produced lazily (one at a time)

import math

s = [25, -16, 9, 81, -100]

def sqare_root(n):
    return math.sqrt(n)


## c = map(sqare_root(s) ) # give error as we are trying to calculate sqare root of negative number, in this case we can avoid those numbers and get sqare root values of valid numbers.

def is_positive(x):
    if x >= 0:
        return x

c = map(sqare_root, filter(is_positive, a))
print(list(c))