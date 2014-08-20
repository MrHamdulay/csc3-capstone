"""Name: Sibulele Hlongwane
Date: 20 April 2014
Program: Display a list of names, right aligned"""

#Prompts user to enter a string of names
names= input("Enter strings (end with DONE):\n")
x=[]
#Repeat until the user enters the word as Done=Sentinel
while (names!="DONE"):
    x.append(names)    
    names=input()


print()
print("Right-aligned list:")

#Sets counter to 0 for spaces
icount=0
temp= ""

#Determines the longest name in list and stores it as temp
for a in x:
    if len(x[icount])>len(temp):              
        temp=a
    icount=icount+1

#Assigns the length of the longest string
longest=len(temp)
space=0

#Prints string of names, right aligned, with the spaces set as the longest lengthed word minus the length of the name
for a in x:
    print(" "*(longest-len(a)) + a)
       