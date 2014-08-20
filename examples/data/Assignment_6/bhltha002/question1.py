#A program to print out right aligned strings
#Thabang Bhili
#25 April 2014


name=input("Enter strings (end with DONE):\n") #allow input of strings
list=[]
while not name=="DONE":     #repeat as when user has not punched in Done
    list.append(name)
    name=input()
    
maxi=0                        #loop through to find lengh of list and set maximun
for i in list:
    x=len(i)
    if x>maxi:
        maxi=x
        
print()                             #Output
print("Right-aligned list:")
for i in list:
    a="{0:>" +str(maxi)+"}"
    print(a.format(i))
    