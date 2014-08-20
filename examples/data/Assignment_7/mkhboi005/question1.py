""" Tumi Mkhawana
28 April 2014
Assignment 7 Question 1"""

strings= input("Enter strings (end with DONE):\n")
stringlist=[]
uniquelist=[]

while strings != "DONE":
    stringlist.append(strings)
    strings= input("")

print("\nUnique list:")    
for i in stringlist:
    if i not in uniquelist:
        uniquelist.append(i)
        print(i)
