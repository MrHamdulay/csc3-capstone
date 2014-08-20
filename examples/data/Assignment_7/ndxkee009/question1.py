"""Keegan Naidoo
NDXKEE009
27 April 2014"""

list=[]      # Creates an empty list
string=input("Enter strings (end with DONE):\n")
counter=0
while string!="DONE":          #Adds strings to list if they are unique
       if counter==0:   
              string=string 
       else:
              string=input("")
       counter+=1
       if string not in list: 
              list.append(string)
print()
print("Unique list:")
for i in range(len(list)-1):            #Displays new unique list
       print(list[i])