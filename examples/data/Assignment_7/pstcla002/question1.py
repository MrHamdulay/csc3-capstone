"""Ordered list of strings without duplicates
Claudia Pastellides
1 May 2014"""

lst1=[]
string=input("Enter strings (end with DONE):\n")
while string!="DONE": #conditional loop
    if string not in lst1: #remove duplicates
        lst1.append(string)
    string=input() #continious input
    
print() #leave a line
print("Unique list:")
for i in lst1: #iterate through items in list
    print(i)
    
