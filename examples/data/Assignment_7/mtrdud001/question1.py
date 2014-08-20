"""Printing given words without repeat
Dudley Mutero
1/5/14"""

list1=[]
print("Enter strings (end with DONE):")
val=""
while val != "DONE":
    val=input()
    if val != "DONE" :
        if val in list1:
            continue
        else:
            list1.append(val)
print()

print ("Unique list:")
for i in list1:
    print (i)
        
    



