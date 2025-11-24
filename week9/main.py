"""## Recursion ##"""

## Recursion in Python is a programming technique where a function calls itself in order to solve a problem.
## Each recursive function must have:

# Base Case – the condition under which the function stops calling itself.

# Recursive Case – the part where the function calls itself with a smaller or simpler input.

## This approach is useful for problems that can be broken into smaller subproblems, such as factorials, Fibonacci numbers, tree traversal, etc.

# pythin let's you call the same function within the function.

# sum of n numbers
def sum(n):
    if(n == 1):
        return 1
    else:
        return n + sum(n-1)


#compond interest by assuming the interest to be 10%
def comp(p,n):
    if(n == 1):
        return p*(1.1)
    else:
        return (comp(p, n-1))* 1.1

# calculating factorial 
def fact(n):
    if(n == 1):
        return 1
    else:
        return n * fact(n-1)
    
"""## Binary Search ##"""

##Binary search is a fast searching algorithm used to find an element in a sorted list. It works by repeatedly dividing the search interval in half.

## Steps ##
# Start with a sorted list.
# Find the middle element.
# Compare the middle element with the target value:
   #  If the middle element equals the target → found.
   # If the target is smaller, search in the left half.
   # If the target is larger, search in the right half.
# Repeat the process until the list cannot be divided further.

def binary_search(l,k):
    begin = 0
    end = len(l)-1
    while(end-begin > 1):
        mid = (begin+end)//2
        if(l[mid]==k):
            return 1
        if(l[mid]> k ):
            end = mid-1 
        if(l[mid] < k):
            begin = mid+1
    if(l[begin] == k) or (l[end]==k):
        return 1
    else:
        return 0


"""## Binary search recursively ##"""

def binary_search_recursively(l,k, begin, end):

    if(begin == end):
        if(l[begin] == k):
            return 1
        else:
            return 0
    
    if(end-begin == 1):
        if(l[begin]== k) or (l[end] == k) :
            return 1
        else:
            return 0
    
    if(end-begin>1):
        mid = (end+begin) // 2
        if(l[mid] > k):
            end = mid-1
        if(l[mid] < k):
            begin = mid+1
        if(l[mid] == k):
            return 1
    
    if(end-begin < 0):
        return 0
        
    return binary_search_recursively(l,k, begin, end)