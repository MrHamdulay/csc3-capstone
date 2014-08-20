"""Assignment 6, Question 1 Creating a list
Duncan Saffy 
20 April 2014"""
strings=input("Enter strings (end with DONE):\n")
l=[]
while strings!= "DONE":
    
    l.append(strings)
    strings=input("")
    

for i in range(len(l)):
    maxlength=len(l[0])
    if len(l[i]) > maxlength:
        maxlength= len(l[i])
    else: continue 

print()
print("Right-aligned list:")
    
for j in range(len(l)):
    print(l[j].rjust(maxlength))