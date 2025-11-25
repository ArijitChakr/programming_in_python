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

def non_decreasing(L):
    """
    A recursive function that determines if L is sorted in non-decreasing order.

    Parameters: 
        L: list of integers
    Return:
        result: bool
    """
    if(len(L) <= 1 ):
        return True
    if(L[0] <= L[1]):
        return non_decreasing(L[1:]) 
    else:
        return False
        
def uniq(L):
    """
    A recursive function to get unique elements from the list. 
    must retain the last occurrence of each distinct element in the list.
    
    Parameters:
        L: list
    Return:
        result: list
    """
    if(len(L) <= 1):
        return L[:]
    rest = uniq(L[1:])
    if(L[0] in rest):
        return rest
    else:
        return [L[0]] + rest
    
def search(L, k):
    """
    A recursive function that searches for an element k in L.

    Parameters:
    	L: list
    	k: int
    Return:
    	bool
    """
    if(len(L) == 0):
        return False
    if(len(L) == 1):
        return L[0] == k
    mid = len(L) // 2
    if(k == L[mid]):
        return True
    if(k > L[mid]):
        return search(L[(mid+1):], k)
    if(k < L[mid]):
        return search(L[:mid], k)

"""## Insertion sort ##"""
def insert(L, x):
    """
    Insert x in L

    Parameters:
        L: list of sorted integers
        x: integer
    Return:
        result: sorted list of integers
    """
    res = []
    inserted = False
    for v in L:
        if not inserted and v >= x:
            res.append(x)
            inserted = True
        res.append(v)
    if not inserted:
        res.append(x)
    return res

def isort(L):
    """
    A recursive function to sort the list L

    Arguments:
        L: list of integers
    Return:
        result: sorted list of integers
    """
    if(len(L) <= 1):
        return L
    sorted_list = isort(L[:-1])
    
    return insert(sorted_list, L[-1])
    

def poly(L, x_0):
    """
    A recursive function to compute the value of a polynomial.

    Parameters:
        L: list of integers
        x_0: integer
    Return:
        result: integer
    """
    if(len(L) == 0):
        return 0
    if(len(L) == 1):
        return L[0] 
    else:
        return (L[-1] * (x_0 ** (len(L)-1))) + poly(L[:-1], x_0)  
    
""" ## Matrix multiplication ## """

def power(A, m):
    """
    A recursive function to compute A ** m.

    Parameters:
        A: list of lists
        m: integer
    Return:
        result: list of lists
    """
    if m == 1:
        return A
    
    return matrix_multiply(A, power(A, m-1))

def matrix_multiply(A, B):
    n = len(A)
    def dot_product(i, j, k):
        if k == n:
            return 0
        return A[i][k] * B[k][j] + dot_product(i, j, k + 1)

    def compute_row(i, j):
        if j == n:
            return []
        return [dot_product(i, j, 0)] + compute_row(i, j + 1)

    def build_matrix(i):
        if i == n:
            return []
        return [compute_row(i, 0)] + build_matrix(i + 1)

    return build_matrix(0)
    

def subset_sum(L, s):
    """
    A recursive function to determine the presence of a subset with sum s.

    Parameters:
        L: list of integers
        s: integer
    Return:
        result: bool
    """
    if s == 0:
        return True
    if not L:
        return False

    include = subset_sum(L[1:], s - L[0])

    exclude = subset_sum(L[1:], s)

    return include or exclude

def det(M):
    """
    A recursive function to compute the determinant of M.
    
    Parameters:
        M: list of lists
    Return:
        result: integer
    """
    n = len(M)

    if n == 1:
        return M[0][0]

    if n == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]

    result = 0
    for j in range(n):
        minor = []
        for r in range(1, n):
            row = M[r][:j] + M[r][j+1:]
            minor.append(row)
        result += ((-1)**j) * M[0][j] * det(minor)

    return result


def collatz(n):
    """
    A recursive function to compute the number of calls to the Collatz function of n

    Argument:
        n: integer
        Assume that 1 < n <= 32,000
    Returns: 
        result: integer
    """
    if(n == 1):
        return 0
    else:
        if(n%2 == 0):
            return 1 + collatz(int(n/2))
        else:
            return 1 + collatz(3*n + 1)
        

def linear(P, Q, k):
    """
    A recursive function to determine if a list is scalar multiple of the other

    Arguments:
        P: list of integers
        Q: list of integers
        k: integer
    Return:
        result: bool
    """
    if(len(P) != len(Q)):
        return False
    else:
        if(len(P) <= 1):
            return P[0] == (Q[0] *k)
        else:
            if(P[0] == (Q[0] * k)):
                return linear(P[1:], Q[1:], k)
            else:
                return False
            

def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps 

    Argument:
        n: integer
    Return:
        result: integer
    """
    if(n == 0):
        return 1
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    return steps(n-1) + steps(n-2) + steps(n-3)

