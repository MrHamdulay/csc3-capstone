"""Assignment 7, question 1: unique list
Duncan Saffy
27 April 2014"""
x=input("Enter strings (end with DONE):\n")
listt=[]
while x!="DONE":
    listt.append(x)
    x=input("")
for i in listt:
    if listt.count(i)==1:
        continue
    else: 
        listt.reverse()
        while listt.count(i)!=1:
            listt.remove(i)
        listt.reverse()

print()
    
print("Unique list:")
for i in listt:
    print(i)