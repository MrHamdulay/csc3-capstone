#This program prints out the strings entered in by the user with the correct spacing so that all strings are lined up
#Ali Goldstein
#24 April 2013

#prompting the user to enter strings
strings=input("Enter strings (end with DONE): \n")
longest=0
list=[]

#adding the string onto the end of the list
while strings!="DONE":
    list.append(strings)
    strings = input("")

#searching for the longest string   
for i in list:
    x=len(i)
    if (x>longest):
        longest=x

#printing the right-aligned list    
print()
print("Right-aligned list:")
for i in list:
    print((" "*(longest-len(i)))+i)