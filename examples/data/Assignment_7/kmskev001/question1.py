"""program to reproduce a list wihtout duplicates
   kevin kumasamba
   01 may 2014"""

# get strings that must be converted into a list

string_list=[]
new_string_list=[]

strings=input("Enter strings (end with DONE):\n")
while strings!="DONE":
    string_list.append(strings)
    strings=input()
    
# check if there are any duplicates within a string and delete them

for string in string_list:
    if string not in new_string_list:
        new_string_list.append(string)
                        
print("\nUnique list:")
for string in new_string_list:
    print(string)