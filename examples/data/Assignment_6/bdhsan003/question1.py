# Program asking user to input a list of strings followed by "Done".
#Sandisha Budhal
#BDHSAN003

new_list = [] #creating an empty list

def lis():
    strings=input("Enter strings (end with DONE):\n")
    
    while strings!="DONE":
        new_list.append(strings)
        strings=input("")
    
            
lis()
print()

c=0 #setting the value of c to 0
for i in new_list:
    if len(i)>c:
        c=len(i)
print("Right-aligned list:")

for n in new_list:
    print(" "*(c-len(n))+n)  
        
        

  
