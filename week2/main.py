# variables, a programmers perspective
ram_bank_balance = 100000
ram_loan = 500000

lakshman_bank_balance = 2000000
lakshman_loan = 10000000

net_income = ram_bank_balance+lakshman_bank_balance
net_liability = ram_loan+lakshman_loan

final_value = net_income - net_liability

print("So, the family has", final_value)

# variable revisited: Dynamic typing

a = 10
print(type(a))
a = a/2
print(type(a))
print(a)

a = "india"
print(type(a))

# Variables, expression and operators

# multiple assigning
x, y = 1, 2
print(x, y)

m = n = o = p = 10

print(m,n,o,p)
x,y = y,x
print(x,y)

x = 10
del x, y

#shorthand
count = 0
count += 1 
count *=2
count -= 1 
count /= 1 
print(count)

#"in" operator: returns boolean value based if the first is available in the second statement
print("alpha" in "alpha-numeric character")

#multiple operator in a single line called chaining operators
x = 5
print(1<x<10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)

#Escape characters and type of quotes

# 'it's a beautiful day' - syntax error

print('It\'s beautiful day') #escape character
print("We are from \"IIT\" Madras")
print("My name is Arijit. \tI am from Pune")# tab spacing using "\t"
print("Hi there \n I'm Arijit") # "\n for new line"

x = 'this is a string'
y = "This is also a string"
z = '''first line  
second line
third line''' # ''' is used for multi line string and multi line comment

# String methods
x = "PytHOn strING methods"

# lower() : converts a string to lower case chracter
print(x.lower())

#upper() : Converts a string into upper case characters
print(x.upper())

#capitalize() : converts only the first character into upper case
print(x.capitalize())

#title() : converts first character of each word to uppercase
print(x.title())

#swapcase() : swap the cases of the characters i.e, lower case becomes upper case and vice versa
print(x.swapcase())

#isLower() : returns true if all characters in the string are lower case
print(x.islower())

#isupper() : returns true if all characters in the string are in upper case
print(x.isupper())

#istitle() : returns true if the string follows the rule of a title like every word starts with a capital letter
print(x.istitle())

#isdigit() : returns true if all characters in the string are digits
y = "123"
print(y.isdigit())

#isalpha() : returns true if all the characters are Alphabets
y = "abc"
print(y.isalpha())

#isalnum() : returns true if all the characters in the string are alpha numeric. Not true for special characters(*@#%)
y = "123abc"
print(y.isalnum())

#strip() : returns a trimmed version of the string
y = "---Python---"
print(y.strip("-"))

#lstrip() : returns a left trim version of the string
y = "---Python---"
print(y.lstrip("-"))

#rstrip() : returns a right trim version of the string
y = "---Python---"
print(y.rstrip("-"))

x = "Python"
print(x.startswith("P")) # returns true if string starts with the given value
print(x.endswith("P")) # returns true if string ends with the given value
#Note: these 2 methods are case sensitive

x = "Python string methods"
#count() : returns the number of times a specified value occurs
print(x.count("t")) 

#index() : searches the string for a specified value and returns the position of where it was found, if multiple returns the first occurance value
print(x.index("t"))

#replace() : Returns a string where a specified value is replaced by another given value
print(x.replace("s" ,"S"))

### An Interesting Cipher: More on string ###

alpha = 'abcdefghijklmnopqrstyz'
i = 27
#print(alpha[i])
#print(alpha(i + 1))
print(alpha[i%26])

#this is popularly called as the "Caesar cipher" in cryptography
name = "arijit"
#expected output "bsjkju" : shifting 1 letter from the characters
t = ''
i = 0
k = 1
t = t + (alpha[(((alpha.index(name[i])+k)%26))])
t = t + (alpha[(((alpha.index(name[i+1])+k)%26))])
t = t + (alpha[(((alpha.index(name[i+2])+k)%26))])
t = t + (alpha[(((alpha.index(name[i+3])+k)%26))])
t = t + (alpha[(((alpha.index(name[i+4])+k)%26))])
t = t + (alpha[(((alpha.index(name[i+5])+k)%26))])
print(t)


### Intro to IF statement ###
print("date of birth")
birth_year = int(input())

current_year = 2025

age = current_year - birth_year

if (age < 18) : 
    print("You are a Minor")
else : 
    print("You are an adult")    


