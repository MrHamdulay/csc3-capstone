""" Bella Gorham
unique list function
29/04/14"""

string = ""
unique_list = []
print("Enter strings (end with DONE):")
while string != "DONE":
    string = input()
    if string not in unique_list:
        unique_list.append(string)
    else:
        continue
unique_list.remove("DONE")
print("\nUnique list:")
for i in unique_list:
    print(i)
    
    