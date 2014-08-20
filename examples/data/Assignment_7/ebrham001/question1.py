'''Program where a list of strings is echoed back without duplicates
HAMZA EBRAHIM
02/05/2014'''

# Assignment 7 - Question 1

# initialize two new lists

mylist = []

new = []

# prompt user for strings as input

sentence = input("Enter strings (end with DONE):\n")

# set sentinel condition for while loop and append strings to first list

while sentence != 'DONE':
    mylist.append(sentence)
    sentence = input('')
print()     

# copy contents of mylist into new; if contents already exist in new will not copy

for i in mylist:
    if i not in new:
        new.append(i) 

# print output of new

print("Unique list:")    
l = '\n'.join(new)    
print(l)