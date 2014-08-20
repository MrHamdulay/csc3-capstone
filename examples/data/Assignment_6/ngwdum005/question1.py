"""Dumisani Ngwenza
NGWDUM005
21/04/2014
Assignment 6 Question1"""

#create an empty string
names_list = []

#allows user to input strings
name = input("Enter strings (end with DONE):\n")
#names_list.append(name)

while name!= 'DONE':
    if name == 'DONE': 
        break
    names_list.append(name)
    name = input()
print()
print ("Right-aligned list:")

#to align letters
max = 2
for i in names_list:
    length = len(i)
    if length> max:
        max = length

#returns a right-aligned list
for i in names_list:
    print (' '*(max - len(i)), i, sep='')