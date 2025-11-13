#Even or odd
num = int(input("Enter a number: "))

if (num % 2 == 0): 
    print(num, " is an even number")
else: 
    print(num, "is odd number")

#num ends with 0,5 or any other number
num = int(input("Enter a number: "))

if (num % 5 == 0 and num % 2 != 0):
    print(num, " ends with 5")
elif(num % 10 == 0 ):
    print(num, " ends with 0")
else: 
    print(num, " ends with other than o or 5")


# find grades: A : >= 90, B: >=80 and <90, C: >=70 and <80, D: >= 60 and <70, E: <60

marks = int(input("Enter your marks: "))

if(marks > 100 or marks < 0): 
    print("Invalid input")
elif(marks >= 90) : 
    print("Your grade is A")
elif(80 <= marks < 90):
    print("Your grade is B")
elif(70 <= marks < 80):
    print("Your grade is C")
elif(60 <= marks < 70):
    print("Your grade is D")
else:
    print("Your grade is E")

# Convert the given flowchart into a python code

print("Travel from city A to city B")
time = int(input("Enter time: "))
longer = int(input("Define longer: "))

if(time >= longer): 
    train_higher = int(input("Definer train higher: "))        
    train_price = int(input("Enter train price"))

    if(train_price >= train_higher):
        print("Train")
    else:
        print("Coach")    
else: 
    flight_price = int(input("Enter flight price: "))
    flight_higher = int(input("Define higher: "))
    
    if(flight_price >= flight_higher):
        print("Daytime Flight")
    else: 
        print("Red Eye flight")    
print("Arrive city B")