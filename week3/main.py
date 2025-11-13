# while loop
ans = False

while(ans == False):
    print("When did India get it's independence (year)?")
    year = int(input())

    if(year == 1947):
        print("correct answer")
        ans = True
    else: 
        print("wrong answer, try again")


#For loop

#range(count of running loop)
for i in range(10):
    print("Hello world")

#range(starting point(if not mentioned default value is 0), ending point, steps(if not mentioned default value is 0))
for i in range(1, 11, 2):
    print(i)

#from higher to lower number(9-0)

for x in range(9, -1, -1):
    print(x)

#for loop without range
country = "India"
for letter in country:
    print(letter)

#Formatted printing

#printing in a single line, print statement default value is: "\n"
for x in range(10):
    print(x, end = " ") #print(val, end =) ending format of print function

# seperation in print statement, print function default seperation value is space(" ")
d = 13
m = 10
y = 2025
print("Today's date is", end = " ")
print(d, m, y, sep = "/") # sep = char , seperation character of print statement after a ",", default value space(" ")

# f'{var} string': f'' stands for formatted printing

num = 2

for i in range(1, 11):
    print(f'{num} X {i} = {num * i}')


# print using format function:  '{index}'.format(index_value)
for i in range(1, 11):
    print('{0} x {1} = {2}'.format(num, i, num * i))

#### Print using string modular operator #####
#old way of writing print statement format supported in C language
for i in range(1, 11):
    print('%d x %d = %d' % (num, i, num * i)) # (" %d " stands for index, % , (index_values seperated by ",") 


##format specifiers ##

pi = 22/7

print(f'value of PI = {pi:.2f}') # :.2f stands for upto 2 decimal point number
print('Value of PI = {0:.2f}'.format(pi))
print('Value of PI = %.2f' % (pi))


## pattern printing ##

# :5d, 5 specifies minimum number of spaces required if not filled with characters at the begining of the statement, 'd' stands for integer
print("{0:5d}".format(1))
print("{0:5d}".format(11))
print("{0:5d}".format(111))
print("{0:5d}".format(1111))
print("{0:5d}".format(11111))

# when we know the total number of times loop should run we should use for loop, and when we don't know the total number of times a loop should run we can use while loop

### Nested while loop ###

s = "VIBGYOR"
t = "VIBGYOR"

for i in range(7):
    for j in range(7):
        print(s[i], s[j])


### break , continue and pass ###

## break: "break" is used to get out of the loop iteration and stop execution at a given point before full execution of the loop

# accept email of an user and output the username part of the email
# input: xyz123@iitm.in , output: xyz123

email = input("Enter your email: ")
username = ""
for l in email: 
    if(l == "@"):
        break
    username += l
print(username)


## continue: continue is used if we wish not to execute a specific iteration of the loop and continue from the next iteration

email = input("Enter your email: ")
username = ""
domain = ""
isDom = False 
for l in email:
    if(l == "@"):
        isDom = True
        continue
    if(not isDom):
        domain += l
    else:
        username += l    
print(username, domain)

## pass: The 'pass' statement in Python is used as a placeholder for future code. When Python encounters it, it simply continues to the next line without performing any action. Without 'pass', having an empty block would cause a SyntaxError, because Python requires at least one statement inside the block.'pass' satisfies that requirement without affecting program logic.

for x in range(11):
    if(x%3 == 0):
        print(x)
    else:
        pass

