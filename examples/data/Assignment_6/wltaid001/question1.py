"""Aiden Walton
WLTAID001
Question 1 - Assignment 6"""

#Ask user to enter set of srings
list=[]
maxword=0
raw_input=input("Enter strings (end with DONE):\n")
while raw_input!="DONE":
    list.append(raw_input)
    raw_input=input("")
    
#Process strings
for word in list:
    if len(word)>maxword:
        maxword=len(word)
    else:
        continue
    
#Allign strings based on longest string
print()
print('Right-aligned list:')
for word in list:
    space=maxword-len(word)
    print(" "*space,end="")
    print(word)
    