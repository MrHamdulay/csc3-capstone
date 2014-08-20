'''Program to print out a unique list
Mahnoor Ahmed
30 April 2014'''

strlist=[]
finlist=[]
instr=input("Enter strings (end with DONE):\n")
strlist.append(instr)
while instr != "DONE":
    instr=input("")
    strlist.append(instr)
    
else:
    del strlist[-1]                                         #deleting "DONE" from the list
    print("\nUnique list:")
    for i in strlist:
        if i not in finlist:                                #creating a seperatelist without any duplicates
            finlist.append(i)
            print(i)
    