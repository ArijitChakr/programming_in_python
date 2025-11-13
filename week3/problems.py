
#factorial using while loop

num = int(input("Enter your number: "))

fact = 1
if(num < 0) :
    print("Not defined")
else:
    while( num > 0):
        fact *= num
        num -= 1
    print("factorial value is: ", fact)


#find the number of digits in the given number

num = abs(int(input("Enter your number: ")))

count = 0

if(num == 0):
    count = 1
else:
    while(num > 0):
        num //= 10
        count += 1
print("Number of digits are: ", count)



# reverse the digits of a given number
num = int(input("Enter your number: "))

absNum = abs(num)
rev = absNum % 10 
absNum //= 10

while(absNum > 0):
    r = absNum % 10
    absNum //= 10
    rev = rev * 10 + r

if(num > 0 ):
    print(rev)
else:
    print(-rev)
    

# given number is palindrom or not

num = abs(int(input("Enter your number: ")))

copyNum = abs(num)
rev = copyNum % 10 
copyNum //= 10

while(copyNum > 0):
    r = copyNum % 10
    copyNum //= 10
    rev = rev * 10 + r

if(rev == num):
    print("Palindrom")
else:
    print("not palindrom")

#for loop for some n numbers

n = int(input("Enter a number: "))

sum = 0

for i in range(n):
    # sum += (i+1) #exclude 0
    sum += i #including 0

print(sum)


# for loop for multiplication tables with starting point of range

n = int(input("Enter table number: "))

for i in range(1,11): #range(starting point, ending point)
    print(n, " x ", i, " = ", (n*i) )

# factorial using for loop

num = int(input("Enter your number: "))

fact = 1
if(num < 0) :
    print("Not defined")
else:
    for i in range(num, 1, -1): # for i in range(1,num+1):
        fact *= i
    print("factorial value is: ", fact)


### Nested loops problems ###

#for loop for multiplication tables upto 9

for i in range(1,10):
    for k in range(1,11):
        print(i, " x ", k, " = ", (i*k))
    print("-"*10)


# Find all prime numbers less than the entered number #

num = int(input("Enter your number: "))

if(num > 2):
    print(2, end = " ")
for i in range(3,num):
    flag = False
    for j in range(2, i):
        if(i%j == 0):
            flag = False
            break
        else:
            flag = True
    if(flag):
        print(i, end = " ")

# find the total profit/loss of each trader working in a trading firm. Information regarding the number of traders and number of transactions are unknown.
##employee input should end when we receive input as -1 and transaction acceptance should end when we receive input as 0

empId = input("Enter employee ID: ")
while(empId != '-1'):
    trade = int(input("Enter the trade amount: "))
    profit_loss = 0
    while(trade != 0):
        profit_loss = profit_loss + trade
        trade = int(input("Enter the trade amount: "))
    print(f'Profit/loss for {empId} is {profit_loss}')
    empId = input("\nEnter employee ID: ")


# Find the daywise total rainfall for the entered duration of time e.g week month etc.
## get total number of days as input and then rainfalls for each day as input until we get rainfall input as -1 , output should be total number of rain in each day

total_days = int(input("Enter total number of days: "))
for i in range(1, total_days+1):
    rainfall = int(input("Enter rainfall amount: "))
    total_rainfall = 0
    while(rainfall != -1):
        total_rainfall += rainfall
        rainfall = int(input("Enter rainfall amount: "))
    print(f'Total rainfall for day {i} is {total_rainfall}')


# Find the length of the longest word from the set of words entered by the user

word = input("Enter a word: ")
maxLen = 0
while(word != "-1"):
    word_count = 0
    for letter in word:
        word_count += 1
    if(word_count > maxLen): 
        maxLen = word_count
    word = input("Enter a word: ")
print("THe length of longest word is %s" %maxLen)



## accept email of an user , where first half before "@" is the username and after is the domain. output should be the username and domain from the email

email = input("Enter your email: ")
username = ""
domain = ""
isDom = False 
for l in email:
    if(l == "@"):
        isDom = True
        continue
    if(not isDom):
        username += l
    else:
        domain += l

print(f'username: {username} , domain: {domain}')

