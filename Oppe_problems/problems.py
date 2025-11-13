'''Check if a string is a palindrome with odd length.

    Args:
        s : str - input string

    Returns:
        bool - True if s is a palindrome with odd length, False otherwise.
'''
'''def is_odd_length_palindrome(s: str) -> bool:
    if(len(s) == 1):
        return True
    reverse_s = s[::-1]
    if(reverse_s == s and len(s) % 2 == 1):
        return True
    else :
        return False
    
print(is_odd_length_palindrome("racecar"))'''


"""Given the data of student marks in the format of list of tuples of format (rollno:str, marks:int), write a function to filter student roll numbers based on the following criteria:

    • 'above_average': Students with marks above or equal to the average.

    • 'below_average': Students with marks below the average.

    • 'fail': Students with marks less than 40.

    • 'toppers': Students with marks 90 or above.

    • None: Return all roll numbers.

    • Any other value should return None.

The order of the roll numbers in the filtered roll numbers should be same as they appear in the data.
"""
'''
def get_roll_nos(data:list, criteria=None):
    sum_marks = 0
    for _, mark in data:
        sum_marks += mark

    average_mark = sum_marks / len(data)
    
    if(criteria == "above_average"):
        return [roll for roll, mark in data if mark >= average_mark]
    
    elif(criteria == "below_average"):
        return [roll for roll, mark in data if mark < average_mark]
    
    elif(criteria == "fail"):
        return [roll for roll, mark in data if mark < 40]
    
    elif(criteria == "toppers"):
        return [roll for roll, mark in data if mark >= 90]
    elif(criteria == None):
        return [roll for roll, _ in data]
    
    else:
        return None
        
data  = [('101', 55), ('102', 25), ('103', 40), ('104', 45), ('105', 35)]
print(get_roll_nos(data, 'fail'), ['102', '105'])
print(get_roll_nos(data, 'below_average'), ['102', '105'])
print(get_roll_nos(data, 'above_average'), ['101', '103', '104']) 
'''        

'''
Given an integer n (where n > 0), print a "V" shaped pattern with n rows. The pattern should use backslashes (\) and forward slashes (/) for each row, with the v character at the bottom. There should be no spaces to the right of the pattern.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format

    • A single integer n, representing the number of rows in the pattern.

Output Format

    • A "V" shaped pattern with n rows, as described.

Constraints

    • 1 <= n

Examples

Input:

1
Output:

v
Input:

2
Output:

\ /
 v
Input:

3
Output:

\   /
 \ /
  v
'''

'''n = int(input())

for i in range(1, n):
    print(" "*(i-1) + ""+" " * (2 * (n-i)-1) + '/')

print(' ' * (n-1) + "v")'''
        

'''Check if the string is enclosed with double quotes and has double quotes inside.

    Args:
        s : str - input string

    Returns:
        bool - True if the string starts and ends with double quotes and has double quotes inside
'''
'''def within_and_has_double_quotes(s: str) -> bool:
    if(s[0] == '"' and s[-1] == '"' and '"' in s[1:-1]):
        return True
    else:
        return False
'''    

'''
    Replace the middle element of a tuple with `n` copies of the middle element.

    Args:
        t (tuple): A tuple with an odd number of elements.
        n (int): The number of times the middle element should be repeated.

    Returns:
        tuple: A new tuple with the middle element replaced by `n` copies.
'''

'''def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    middle_t = len(t) // 2
    
    middle_el = t[middle_t]
    
    l = []
    
    for i  in t:
        if(i == t[middle_t]):
            for j in range(n):
                l.append(i)
        else:
            l.append(i)
    
    return tuple(l)    
'''

def walk_matrix(M, shape):
    """
    Walk along the matrix M according to the specified shape and return the path.

    Args:
        M (list of lists): The square matrix.
        shape (str): Path shape, one of "L", "O", or "Z".

    Returns:
        list: Path along the matrix according to the shape.
    """
    n = len(M)
    new_list = []
    if(shape == "L"):
        for i in range(n):
            if(i == (n-1)):
                for k in range(n):
                    new_list.append(M[i][k])
            else:
                new_list.append(M[i][0])
    elif(shape == "Z"):
        for i in range(n):
            new_list.append(M[0][i])
        for j in range(1, n-1):
            new_list.append(M[j][n-j-1])
        for k in range(n):
            new_list.append(M[n-1][k])

    elif(shape == "O"):
        for i in range(n):
            new_list.append(M[0][i])
        
        for k in range(1, n-1):
            new_list.append(M[k][n-1])
        
        for j in range(n-1, 0, -1):
            new_list.append(M[n-1][j])
        
        for o in range(n-1, 0, -1):
            new_list.append(M[o][0])

    return new_list


M = [
    [1, 2, 3,4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]



def mm_dd_yy_to_yy_dd_mm(date: str) -> str:
    """
    Convert a date string from the format mm-dd-yy to yy-dd-mm.

    Args:
        date (str): The date in the format "mm-dd-yy".

    Returns:
        str: The date in the format "yy-dd-mm".

    Example:
        >>> mm_dd_yy_to_yy_dd_mm("12-25-21")
        "21-25-12"
    """
    l = date.split("-")
    new_date = ''
    for i in range(len(l), 0, -1):
        if(i == 1):
            print(l[0])
            new_date += l[0]
        else:
            new_date += l[i-1] + "-"
    
    return new_date


def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.

    Note: indices starts from 0.

    Arguments:
    string: str - the input string

    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    '''
    return_log = False
    for i in range(len(string)):
        if(i%2 == 0):
            if(string[i].isdigit()):
                return_log = True
            else: 
                return_log = False
                break
        else:
            if(string[i].isalpha()):
                return_log = True
            else: 
                return_log = False
                break
              
    return return_log

#print(is_odd_indices_alpha_and_even_indices_digits("3x4b6d"))
#print(is_odd_indices_alpha_and_even_indices_digits("123abc"))



def most_occuring_first_letter(passage: str) -> str:
    
    words = passage.lower().split()
    word_c = {}

    for word in words:
        first = word[0]
        if first.isalpha():  
            word_c[first] = word_c.get(first, 0) + 1

    if not word_c:
        return ""

    # Find the most frequent first letter
    max_occ = max(word_c, key=word_c.get)
    return max_occ


p = '''
This is a test sentence where I wanted
to let you know that the sentences are 
multi-line and words are separated by spaces.
The first letters may be of different case but you
should consider it as lowercase and return the lowercase
letter as the result. Also check the other test cases
where you can easily count the most occuring first letter.
'''

#print(most_occuring_first_letter(p))



def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict): 
        a dictionary where keys are student roll numbers and 
        values are lists of courses they chose

    Returns:
    list: 
        a list of courses sorted by the number of students enrolled 
        in descending order
    '''
    course_taken = {}
    
    for courses in student_courses.values():
        
        for course in courses:
            if(course in course_taken):
                course_taken[course] += 1
            else:
                course_taken[course] = 1
    
    course_list = sorted(course_taken, key=lambda k: course_taken[k], reverse=True)
    
    return course_list
    

student_courses1 = {
    '101': ['Math', 'Science'],
    '102': ['Math'],
    '103': ['Science', 'Math'],
    '104': ['Math', 'History'],
    '105': ['English', 'History', 'Science']
}

courses_sorted_by_enrollment(student_courses1)
