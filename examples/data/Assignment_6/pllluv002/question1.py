"""STRING ALIGNMENT TASK
4/21/2014
LUVESHEN PILLAY"""


#Populate list

namelist=[]
a=""
while a != "DONE":
    if a == "":
        a=input("Enter strings (end with DONE):\n")
    
    if a != "DONE":      
               namelist.append(a) 
               a=input("")
long=0               
for i in range(len(namelist)):
    
    if long < len(namelist[i]):
       long = len(namelist[i])
        
#Print list    

print("\nRight-aligned list:")

for i in namelist:
    print("{0:>{1}}".format(str(i),long))