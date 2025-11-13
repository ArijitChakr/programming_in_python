'''## Functions ##'''

# defining functions
def add(a, b): # function  definition starts with def
    ans = a + b
    return(ans) # return statement
print(add(1, 2))  # function call

# functions on lists

# minimum value of a list of integers

def list_min(l):
    minimum = l[0]

    for i in range(len(l)):
        if (l[i] < minimum):
            minimum = l[i]
    return minimum

'''## Types of function arguments ##'''

# keyword arguments #
# we can explicitely mention parameter value using assignment operator, this does not require us to maintain the order of the argument passed to a function

def fun(c, a = 20, b = 30):
    return(a + b - c)
print(add(20, 30, 40))
print(add(a = 20, b = 30, c = 40))

# default arguments #
# if we don't pass all the parameters to the function when calling it throughs an error, to overcome this one can set default values of a parameter while defining the function, so that even if all the parameters are not passed while calling the function it does not through any error
# However we can still pass values to the parameters for which we have mentioned default values
print(add(40))

'''## Types of functions ##'''

# in-built functions: 
print(), input(), len()

# library functions: log(), sqrt(), random(), randrange(), calender(), month()

# String methods: upper(), lower(), strip(), count(), index(), replace()

# User defined functions:
def sqaure(x):
    sqr = x ** 2
    return sqr
