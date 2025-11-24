''' Find 0 in a list using recursion, 
returns 1 if "0" is present else returns 0
'''

def check0(l):
    if(len(l) == 0):
        return 0
    if(l[0] == 0):
        return 1
    else:
        return check0(l[1:len(l)])
## the above code is not an efficient code
## Why the code is inefficient
# Uses slicing (l[1:]):	Creates new lists → O(n²) time
# Deep recursion:	High memory usage → possible stack overflow
# No tail optimization:	Recursion overhead → slower than loops

def check0_efficient(l, i = 0):
    if(i == len(l)):
        return 0
    if (l[i]== 0):
        return 1 
    else:
        return check0_efficient(l, i+1)
    
""" Sorting a list recursively"""

def mini(l):
    m = l[0]
    for x in l:
        if(x<m):
            m = x
    return m

def sort(l):
    if(l == [] or len(l) == 1):
        return l
    m = mini(l)
    l.remove(m)
    return [m]+sort(l)


"""Consider a positive integer x that is a power of 2. The logarithm of x to the base 2 is the number of times 2 has to be multiplied with itself so get x, and is denoted by log2(x). For example, log2(4)=2. Note that log2(1)=0. Write a recursive function named logarithm that accepts this positive integer x as argument and returns log2(x)."""

def logarithm(x):
    """
    A recursive function to compute the log of x
    Parameters:
        x: integer
    Result:
        result: integer
    """
    if(x == 1):
        return 0
    else:
        return 1 + logarithm(x//2)
    

def palindrome(word):
    """
    A recursive function to determine if a string is a palindrome.

    Parameters:
        word: string
    Return:
        result: bool
    """
    if(len(word) == 1):
        return True
    if(len(word) == 2):
        return word[0] == word[len(word)-1]
    if(len(word) > 2):
        return palindrome(word[1:-1])

def count(L, word):
    """
    A recursive function to compute the frequency of occurrences of word in L.

    Parameters:
        L: list of words
        word: string
    Return:
        result: integer
    """
    if(len(L) == 0):
        return 0
    if(L[0] == word):
        return 1 + count(L[1:], word)
    else:
        return count(L[1:], word)