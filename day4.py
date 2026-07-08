"""
Day 4 - Python Data types
Author: Krish
Goal: Learn List , Tuple , Set , Dictionary
""" 

# 1.List - Lists are used to store multiple items in a single variable.
list =  ["khushi", "diya", "krish"]
print(list)
print(list[2])# user can access the single item of list by using index starts from 0
#  lists are ordered , changeable and allow duplicates
print(len(list))#len keyword used to know the items in list 
# List items can be of any data type:
list_1 = ["apple","cherries","orange"]
list_2 = [11,22,33]
list_3 = [True,False,True]
list_4 = ["krish", 19 , True]

print(type(list_4[1]))

# negative indexing
thelist = [1,12,13,5,42,2,11]
print(thelist[-1],thelist[-1])


#range helps to return specific range of items - 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:6])

# Check if Item Exists
if "cherry" in thelist:
    print("yes cherry is present in list")


# Change Item Value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thelist[1]= "grapes"
print(thelist[1])

# Change a Range of Item Values
thislist[2:4] = ["lichi" , "pineapple"]
print(thislist)


# user can insert new items into list and the length of list will also increase - 
mylist = ["krish" , "19" ,"BCA"]
mylist[1:3] = [19,"Male"]
print(mylist)

# Python - Add List Items
# add an item to the end of the list, use the append() method - 
newlist = ["car" , "bike" ,"ship"]
newlist.append("train")
print(newlist)


# To insert a list item at a specified index, use the insert() method.
newlist.insert(1,"cycle")
print(newlist)

# To append elements from another list to the current list, use the extend() method.
anotherlist = ["men" , "women","children"]
newlist.extend(anotherlist)
print(newlist)

# Python - Remove List Items
# The remove() method  -   the remove() method removes the first occurrence:
newlist.remove("children")
print(newlist)

#  The pop() method removes the specified index.
newlist.pop(2)
print(newlist) #If user do not specify the index, the pop() method removes the last item.


#the del -
# del also work as same pop delete item at specific index but if user do not specify index it will delete whole list
del anotherlist
# print(anotherlist) show an error

# clear keyword - used to empty the list 
newlist.clear()
print(newlist)

# looping in lists
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1

# Sort List Alphanumerically - using sort() method
unsortlist = ["kiwi","mango","apple","orange","grapes"]
unsortlist.sort()
print(unsortlist)

# Sort Descending
unsortlist.sort(reverse=True)
print(unsortlist)

# Tuple -  ordered and unchangeable.
thetuple = ("apple", "banana", "cherry")
print(thetuple)

# Create Tuple With One Item - (need comma after one item ,)
tuple = ("apple" , )
tuple2 = ("apple")
print(type(tuple))
print(type(tuple2))

# rest of things are same as list but tuples are unmutable or unchangeable user can't add or remove any item in tuple 


# Sets - unordered, unchangeable, and unindexed but user can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)
# The values True and 1 , False and 0 are considered the same value in sets
thisset = {"apple", "banana", "cherry", False, True, 0 ,1}
print(thisset)

# Once a set is created, you cannot change its items, but you can add new items.
# Add an item to a set, using the add() method - 
theset = {"apple", "banana", "cherry"}
theset.add("grapes")
print(theset)

# update is used to add any literable to the set it can be any set , list , tuple , dictionary -
oneset = {"cars" , " bikes " , "cycle"}
secondset = {"ships" ,"areoplane" ,"trains"}
oneset.update(secondset)
print(oneset)
 

#reomve items in set - remove() , discard() , pop()
oneset.remove("cars")
print(oneset)
# if the item doesn't exist then remove will raise an error 
oneset.discard("elephant")
print(oneset)
# but discard doesn't raise an error
pop = oneset.pop()
print(pop)
# pop removes random item 
print(oneset)


# Dictionaries are used to store data values in key:value pairs -
mydict = {"name" : "krish", "age" : 19,"gender" : "male"}
print(mydict)
print(mydict["age"])
print(mydict.get("name"))
keys = mydict.keys()
print(keys)
mydict["work"] = "student"
print(keys)
# same as values - using values()

# Change Values
mydict["name"] = "krish chhabra"
print(mydict)
mydict.update({"age" : 20})
print(mydict)

# Removing Items - pop , del ,popitem - 
mydict.pop("work")
print(mydict)
mydict.popitem()
print(mydict)
del mydict
# print(mydict)  raise an error  completely deleted by del


# nestd dictionary - 
myfamily = {
  "child1" : {
    "name" : "ishan",
    "year" : 2004
  },
  "child2" : {
    "name" : "hardik",
    "year" : 2007
  },
  "child3" : {
    "name" : "shubman",
    "year" : 2011
  }
}
print(myfamily["child1"])
child1keys = myfamily["child1"].keys()
print(child1keys)
print(myfamily["child2"])
print(myfamily["child3"])

