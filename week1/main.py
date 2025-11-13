#print("hi there")
#print("oyehoyee")
#print("hello world")
#print("hello world", "hello India")
#n=int(input())
#print(n+10)
#10


#r = int(input("enter the radius"))
#area = 3.14 * r * r
#print("Arear of the circle is",area)

# data types
#n = 10 #int
#r = 6.3 #float
#s = "Arijit" #string

#print(type(n), type(r), type(s))

#l = [10, 20, 30] #list

#b1 = True
#print(type(b1))


##type conversion / type casting
#a= int(5.7) #5
#b = int("10") #10
 
#a = bool(10) #true
#b = bool(0) #false
# 0 will give false boolean value but any other number positive and negative integer or float are false

# all string values will give true value if converted to boolean
# an empty string will give false 

#Union
#a = [1.2,3]
#b = [4.5,6]
#arr = a+b
#print(arr) #[1,2,3,4,5,6]

# answer will be 36 due to operator precedence, it will do multiplication as first priority then add.
#n = 10+13*2

#Arithmatic operators (+, - , *, /, //. %, **)

#print("Floor division", 7 // 3) # 2, provides only integer  part
#print("modulus", 7 % 3) # returns remainder
#print("Exponentiation operator", 6 ** 2) # provides exponential value

#Relational operators (>, <, >=, <=, ==, !=)
#returns boolean value

#Logical operators(and, or , not)
#print (True and True)
#print(True and False)
#print(False and True)
#print(False and False)
# "and" operator provides true value if both logics are true else returns false

#print (True or True)
#print(True or False)
#print(False or True)
#print(False or False)
# "or" operator provides true value if atleast one logic is true and only if both logic are false then it returns False

#print(not(True))
#print(not(False))
#"not" operator returns opposite value, like if return value is true not operator will return valse and vice versa.

## Strings ##

s = "coffee"
t = "bread"

print(s[1:3]) # return "of", string slicing.
print(s * 5) # string replication, concatinates multiple times
#string comparison
print(s == "coffee") # true
print(s == "Coffee") # false

print("apple" > "one") #false as apple first letter is "a" and one's first letter is "o", 
print("four" < "ten") # true as "f" comes before "t" alphabatically

print("ab" < "az") # true as b comes before z.
print("abcdef" < "abcde") # false as f cannot be compared to any letter

#negative indexing
print(s[-1]) # give the last letter of s string , and the negative values will return the index value from the end upto length of the string

print(len(s)) # length of string

