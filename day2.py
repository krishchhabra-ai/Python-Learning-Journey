"""
Day 2 - Python Basics
Author: Krish
Goal: Learn data types, operators, and string in Python
""" 
# 1. DATA TYPES -
# data types refer to which type of data we are using there are different types of data which are used by using correct data type
# There are three numeric types in Python:
# ---INT
x=10 
print(type(x)) 
# ---float 
x=20.34
print(type(x)) 
# ---COMPLEX 
x=2j
print(type(x)) 
# type is keyword which is used to display or get the type of data stored in variable
# ---STRING 
x="hello world i am string"
print(type(x)) 
# ---bool
x=True
print(type(x)) 
# ---there are various data types like tuple ,list , dictionary , set used in python 
# ---list 
x=["apple","banana"]
print(type(x)) 
# ---tuple 
x=("apple","banana")
print(type(x)) 
# ---set 
x={"apple","banana"}
print(type(x)) 
# ---dict 
x = {"name" : "krish", "age" : 19}
print(type(x)) 


# 2.OPERATORS - 
# Operators are used to perform operations on variables and values.
print(50 + 50) # + is a operator

# In Python there are various types of the operators :

# Arithmetic operators
# Comparison operators
# Assignment operators
# Logical operators
# Bitwise operators
# Identity operators
# Membership operators


# ---Arithmetic operators are used to perform mathematical operations like - 
a=17
b=3
print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division
print(a%b) # Modulus
print(a**b) # Exponentiation
print(a//b) # Floor division
#   / - Division - returns a float
#  // - Floor division - returns an integer



# ---Assignment operators are used to assign values to variables -
a=3 # a is 3
print(a)
a+=3 # in a - 3 is added
print(a)
a-=2 # in a - 2 is subtracted
print(a)
a*=3 # in a - 3 is multiplied
print(a)
a/=3 # in a - 3 is divided
print(a)
a**=3 # in a - 3 is expenented
print(a)
a//=3 # in a - 3 is floor divided so it returns int
print(a)



# ---Comparison operators return True or False based on the comparison -
a=50
b=40
print("a and b are equal = ",a==b) # Equal
print("a and b are not equal = ",a!=b) # Not equal
print("a is greater than b = ",a>b) # Greater than
print("a is less than b = ",a<b) # Less than
print("a is greater than b or equal = ",a>=b) # Greater than or equal to
print("a is less than b or equal = ",a<=b) # Less than or equal to


# ---Logical operators are check conditions -
# and 	Returns True if both statements are true	
# or	Returns True if one of the statements is true	
# not	Reverse the result
a=10
b=22
print(a < b and b > 20)
print(a > b or b > 20)
print(not a > b) 



# 2.STRINGS -
# strings are created by using single quotas or double quotas but both meaning is same
name = "krish"
name = 'krish'
# both are same 
# user can also assign multiline string using 3 quotas """" , '''
x = """hello my name is 
        krish chhabra 
        and my age is 19 """

# String Length(len) - 
a = "hello world my name is a"
print(len(a)) #The len() function returns the length of a string

# Check String - used to check certain character or word is present in string or not
string = "hello i am a string"
print("hello" in string)
print("world" not in string)

# Slicing -  return a range of characters
name = "krishchhabra"
print(name[2:8])
name = "krishchhabra"
print(name[:8])
name = "krishchhabra"
print(name[2:])
name = "krishchhabra"
print(name[-5:-1])


# modify methods of string - 
# Upper Case
name = "krish chhabra"
print(name.upper())
# Lower Case
print(name.lower())
# strip - used to remove extra spaces from start and end of string
name = "  krish  "
print(name.strip())
# Replace String
name = "brish"
print(name.replace("b","k"))
# split string 
name  = "krish-chhabra"
print(name.split("-"))


# String Concatenation
firstname = "krish"
lastname = "chhabra"
fullname = firstname + lastname
print(fullname)
fullname = firstname + " " + lastname
print(fullname)


# F-Strings
age=19
# name = "hello my name is krish and my age is " + age 
# TypeError: can only concatenate str (not "int") to str
name = f"hello my name is krish and my age is {age}" 
print(name)


# escape character - 
name = "my name is \"krish chhabra\" "
print(name)


