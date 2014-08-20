# A program where the user can enter a list of strings followed by the sentinel "Done"
# Retselisitsoe Monyake
# 20 April 2014

mylist = []
def lis():
    n=input("Enter strings (end with DONE):\n")
    while n!="DONE":
        mylist.append(n)
        n=input("")
    
            
lis()
print()

a=0
for i in mylist:
    if len(i)>a:
        a=len(i)
    

print("Right-aligned list:")
for name in mylist:
    print(" "*(a-len(name))+name)  
        
        

  
