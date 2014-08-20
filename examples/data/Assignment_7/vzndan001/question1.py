"""removing duplicates from given inputs
danica van der zandt
1 may 2014"""

#get an input from the user
strings=[]
string=input("Enter strings (end with DONE):\n")

#add each entered string into a list
while string != "DONE":
    strings.append(string)
    string=input("")
    
#check for duplicates    
non_duplicates=[]
for i in strings:
    if i not in non_duplicates:
        non_duplicates.append(i)
    else:
        continue

#print non_duplicates list, string for string
print("\nUnique list:")
for j in non_duplicates:
    print(j)