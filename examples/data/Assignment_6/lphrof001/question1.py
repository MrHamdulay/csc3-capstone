"""program to print out right aligned list
Author: Rofhiwa Liphauphau
Date: 21 April 2014"""

names=[]#assign the value of an empty string 
answer=input("Enter strings (end with DONE):\n") #prompt user to enter a list of string
while answer!="DONE": #the sentinel is "DONE"
    names.append(answer)
    answer=input("")
    if answer=="DONE":
        break

max=0 #Algorithm to find the longest word for alignment
for word in names:
    length=len(word)
    if length>max:
        max=length
    else:
        continue 

print()

print("Right-aligned list:")#print- heading
for word in names:#print individual inputs in the list
    if len(word)==max:
        print(word)
    else:
        print(" "*(max-len(word)-1),word) #prints spaces according to the length of the word






