"""Akhil Singh
SNGAKH004
30 April 2014"""
#get list of strings
strings=[]
string_list=input("Enter strings (end with DONE):\n")

while string_list != "DONE":
    strings.append(string_list)
    string_list=input ("")
    
new_list = []
for a in strings:
    if a not in new_list:
        new_list.append(a)
        
#Print the new list.
if string_list== "DONE":
    print("\nUnique list:")
    for n in new_list:
        print(n)    
