"""Assignment 7 Question 1 make a unique list of strings
joshua wort
27 april 2014"""

#create the list
lis=[]
string=input("Enter strings (end with DONE):\n")
while string!="DONE":
    lis.append(string)
    string=input("")
    
print()
print("Unique list:")

#create a unique list
unique_list=[]
for string in lis:
    if string not in unique_list:
        unique_list.append(string)

#print the unique list        
for i in range(len(unique_list)):
    print(unique_list[i])
    