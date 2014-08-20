# Program prints a string in the same order of the given string without duplicates
# Wandile Lesejane
# 27 April 2014

string=input("Enter strings (end with DONE):\n")
strings=[]
mylist={}
unique_list=[]

while string!="DONE":
    strings.append(string)
    string=input()
    
for i in strings:
    if i in unique_list:
        continue
    else:
        unique_list.append(i)

print()
print("Unique list:")
for i in unique_list:
    print(i)