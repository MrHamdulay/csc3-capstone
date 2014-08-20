"""Cherise Dube 
27 April 2014
Program to print out input strings with no duplicates"""

strings_list=[]
string=input("Enter strings (end with DONE):\n")

#Creates a list with all input strings
while string!='DONE':
    strings_list.append(string)
    string=input("")

#Makes new string with no duplicates 
strings_list2=[]
for i in strings_list:
    if i in strings_list2:
        continue
    else:
        strings_list2.append(i)

#Prints strings with no duplicates
print()
print("Unique list:")
for j in strings_list2:
    print(j)