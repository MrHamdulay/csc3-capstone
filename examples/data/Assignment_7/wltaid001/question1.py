"""Aiden Walton
WLTAID001
Question 1 - assignment 7"""
stringlist=[]
stringdic={}
string=input("Enter strings (end with DONE):\n")
while string!="DONE":
    if not string in stringdic:
        stringlist.append(string)
        stringdic[string]=0
    string=input("")
print("")
print("Unique list:")
for string in stringlist:
    print(string)
