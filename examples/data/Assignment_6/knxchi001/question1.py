#Assignment 6
#Question 1

#Getting the list of names
list_of_names=[]
name= input("Enter strings (end with DONE):\n")
while name!= "DONE":
   list_of_names.append(name)
   name= input("")
#print(list_of_names)
print()

#Determine which name is the longest
longest_name=0
for name in list_of_names:
   if len(name)>longest_name:
      longest_name=len(name)
   else:
      continue
#print(longest_name)

#Print list aligned to the right
print("Right-aligned list:")
for name in list_of_names:
   space= longest_name-len(name) #Create number of spaces to align the list
   print(" "*space, name, sep="")
   




