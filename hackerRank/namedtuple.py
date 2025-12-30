"""Dr. John Wesley has a spreadsheet containing a list of students IDs , marks,class  and name.

Your task is to help Dr. Wesley calculate the average marks of the students.


Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer , the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, name  and class, under their respective column names.

Constraints
0 < N <= 100

Output Format

Print the average marks of the list corrected to 2 decimal places.
Can you solve this challenge in 4 lines of code or less?
NOTE: There is no penalty for solutions that are correct but have more than 4 lines."""



from collections import namedtuple
n = int(input())
details = namedtuple("details", input().split())
print(f"{sum(int(details(*input().split()).MARKS) for _ in range(n)) / n :.2f}")