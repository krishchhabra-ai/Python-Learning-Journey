"""
Day 2 - Python Control flow
Author: Krish
Goal: Learn  in if, elif, else, nested if, match case, Loops 
""" 

# If statement - 
a=int(input("enter value of a = "))
b=20
if(a<b):
    print("a is less than b") # Indentation Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
# Multiple Statements in If - 
c=18
if(a>=c):
    print("a is adult")
    print("a can apply for driving license")
    print("a can vote")

# Elif statement - "if condition is not true - then elif block execute"
age=int(input("enter you age = "))
if(age >= 21):
    print("you can take part in election")
elif age < 21 and age >= 18:
    print("you can only vote")
elif age < 18:
    print("you can't vote")


# Else statement - The else statement is executed when the if condition (and any elif conditions) are False
marks = int(input("enter your marks = "))
if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 33:
    print("Grade D")
else:
    print("Fail")

# One-line if statement - 
a = 17
b = 9 
if a > b: print("a is greater than")

# Nested If Statements -
x=31
if(x>20):
    print("x is greater than 20")
    if x>30:
        print("x is also greater than 30")
    else:
        print("not greater than 30")


# pass Statement - 
marks=98
if marks > 80:
    pass # sketch out your program structure before implementing the details
print("Access Granted")


# Match Statement - many if..else statements , use the match statement.
day = int(input("enter day btw 1-7 = "))
match day:
    case 1 | 2 | 3 | 4 | 5 :
        print("weekday")
    case 6 | 7 :
        print("weekend")


# LOOPS - while loops , for loops
i = 1
while(i<6): # A while loop keeps executing as long as its condition remains True.
    print(i)
    i+=1 

i=1
while(i<6): 
    print(i)
    if i == 3: 
        break  #Exit the loop when i is 3
    i+=1 
i=1
while(i<6): 
    if i == 3: 
        i+=1 
        continue  #Continue to the next iteration if i is 3
    print(i)
    i+=1 


# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
cars = ["mercedes" , "BMW" , "porche"]
for x in cars:
    print(x)   
# same as while loop user can use break and continue in for loop

# range() Function
for x in range(11):
    if x== 4:
        continue
    print(x)

#user can  give starting and ending point in range -
for x in range(2,9):
    # run only for 2 to 8 
    print(x)
# user can give gap btw iterations also - 
for x in range(2,9,2):
    print(x)

# Else in For Loop -
for x in range(2,9,2):
    print (x)  
else:# else will execute after loop is finished 
    print("done")


# nested loops -
greetings = ["hello" , "how are you" , "what are you doing"]
names = ["krish" , "kapish" , "khushi"]
for x in greetings:
    for y in names:
        print(x,y )


#practice -
#sum of first 10 number -
sum = 0
for i in range(1,11):
    sum += i

print(sum)

#  Find largest of three numbers.
num = int(input("enter a number = "))
if(num % 2==0):
    print(f"{num} is even")
else:
    print(f"{num} is not even")


# Find largest of three numbers.
num1 = int(input("enter a number = "))
num2 = int(input("enter a number = "))
num3 = int(input("enter a number = "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greater than num2 and num3")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is greater than num1 and num3")
else:
    print(f"{num3} is greater than num1 and num2")


"""
Summary

Today I learned:

- if statement
- elif statement
- else statement
- nested if
- pass statement
- match-case
- while loop
- for loop
- break
- continue
- nested loops

Practice Questions:
- Sum of first 10 numbers
- Even/Odd checker
- Largest of three numbers
"""