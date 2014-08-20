"""List of strings 
Claudia Pastellides

23 April 2014"""
names=[]
x=input("Enter strings (end with DONE):\n") 
while x!="DONE": #loop to create items in list
    names.append(x)
    x=input()

print()
max1=0
for i in names: #working out max length of an item in list
    if len(i)>=max1:
        max1=len(i)
print("Right-aligned list:")
    
for j in names: # working out spaces needed using max length
    print(" "*(max1- len(j)),j,end=" ",sep="")
    print()
    
