"""Question 1 - create program to input list, print out list without duplicate additions
Jembe Moran
28 April 2014"""
#create list
unique=[]

#create infinite loop to enter inputs, check for sentinel
x=input("Enter strings (end with DONE):\n")
while x != "DONE":
    if x not in unique: #check if unique
        unique.append(x) 
    x=input("")

#print list    
print()
print("Unique list:")
for i in unique:
    print(i)