"""
Day 1 - Python Basics
Author: Krish
Goal: Learn basic syntax, variables, and user input in Python
""" 
# 1. Printing in Python
print("hello world - My Python Journey Begins")
# print is used to print any thing written inside brackets


# 2. Variables (Storing Data)
# there are variables used in python to store values or data like -
name = "krishchhabra"
age = 19
marks = 99.9
# like this user can store any value there is variable or we can say it like container in which data or values are placed or stored and user can print it or display it by using print.
print(name)
print(age)
print(marks)



# 3. Multiple Variable Assignment
name,age,gender = "krishchhabra",19,"male"
# Python allows you to assign values to multiple variables in one line:
print(name)
print(age)
print(gender)



# 4. Rules of Variables (Examples)
# user can store different types of data in variable like numbers , alphabets and many more but there is no need  to be declared with any particular type, and can even change type after they have been set.
name = "krishchhabra"
# is the same as
name = 'krishchhabra'
# Variable names are case-sensitive.
x = 4
X= "Sally"
#X will not overwrite x
# A variable name cannot be any of the Python keywords.


# 5. User Input (Interactive Program)
# there is one important keyword which is used to take inputs from users to make interactive like 
name = input("enter you name = ")
print("your good name is ",name)


# End of Day 1
print("Day 1 Completed Successfully")