#Assignment 7
#Question 1 


string= input("Enter strings (end with DONE):\n")
string_list=[]
while string!= "DONE":
    string_list.append(string)
    string= input("")

print()
new_list=[]
for string in string_list:
    if string in new_list:
        continue
    else:
        new_list.append(string)
    
print("Unique list:")
for string in new_list:
    print(string)
    
    