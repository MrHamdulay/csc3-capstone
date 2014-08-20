#A program to print unique strings 
#Thabang Bhili
#2014/04/27

X=input("Enter strings (end with DONE):\n")
mylist=[]
while X != "DONE":
    if X not in mylist:
        mylist.append(X)
    X=input()
print("\nUnique list:")    
for y in mylist:
    print(y)
    

    
