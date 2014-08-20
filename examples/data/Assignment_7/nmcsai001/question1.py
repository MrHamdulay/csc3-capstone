"""Saijil Nemchund
NMCSAI001
Program to print strings in an order""" 

old_list=[]  #creating an empty list

a=input("Enter strings (end with DONE):\n") #Asking the user to enter strings

while a!="DONE": 
    
    old_list.append(a) #Adding a to the old list
    a=input() 
    
new=[] #creatiing a new list 
for i in old_list:
    if not i in new: #if new strings are not in old list, add to the list
        new.append(i)
print()
print("Unique list:")       
for j in new:
    print(j) #Printing the new list as a unique list
    