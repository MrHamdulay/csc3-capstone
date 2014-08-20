# Najeeb Sirkhoth
# SRKMOH002
# question1.py
# Assignment 7

# Program which allows user to enter list of strings
# Prints strings without duplicates


# Create empty list    
list1 = []
list2 = []


# While loop which appends users' strings to list
string = input("Enter strings (end with DONE):\n")
while not string == "DONE":                           # Sentinel is "DONE"
    list1.append(string)
    string = input("") 


# for loop which checks if item already in new list, if not, then added    
for i in list1: 
    if i not in list2:
        list2.append(i) 

# Print 
print ("\nUnique list:")
for i in list2:
    print(i) 
