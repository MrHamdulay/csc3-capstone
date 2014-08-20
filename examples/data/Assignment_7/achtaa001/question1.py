# ACHTAA001
# Question1
# prints out list in order of user's input without duplicates

a=input("Enter strings (end with DONE):\n")
lis=[]
while a != "DONE":
    if a not in lis:
        lis.append(a)
    else:
        None
    
    a=input()
    
print()
print("Unique list:")
for i in lis:
    print(i)