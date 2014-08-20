""""program to enter a list of strings and print without repeating
LUCI B*TCH
29 April 2014"""

#get the user to input a list of strings
list=[]
names=input("Enter strings (end with DONE):\n")
list.append(names)
while names!="DONE":
    names=input("")

    if names not in list:
        
            
        list.append(names)

print("\nUnique list:")    
for n in range(len(list)-1):
    print(list[n])
