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