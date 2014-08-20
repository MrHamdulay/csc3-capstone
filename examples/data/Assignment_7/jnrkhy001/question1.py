#Khyati Jinerdeb
#02 May 2014
#Assignment 7
#program to print a listof strings without duplicates

#defines a list
names=[]
name=input("Enter strings (end with DONE):\n")
#using a while loop and a sentinel to end input list
while name!="DONE":
    names.append(name)
    name=input()
    
#defines another list which will eliminate the duplicates
strings=[]
for i in names:
    if i not in strings:    #if the name is not in the list,add it to the new list or else pass
        strings.append(i)
    else:
        pass

print("\nUnique list:")  
for i in strings:
    print(i)
    
    


