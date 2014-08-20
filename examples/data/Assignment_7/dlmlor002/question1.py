"""program to only print out each string in a list no more than once
Lorena Dal Maso
27 April 2014"""

print("Enter strings (end with DONE):")

#create list of strings
string=input("")
string_list=[string]
unique_list=[string]

while string !="DONE":
        if string=="DONE":
                break
        string=input("")
        if string!="DONE":
                string_list.append(string)
                if string not in unique_list:
                        unique_list.append(string)
                                               
print("\nUnique list:")  

#remove "DONE" from unique_list so that if the only input given is "DONE", then unique_list will print nothing
if "DONE" in unique_list:
        unique_list.remove("DONE")
        
#print out each string in unique list
for i in range(len(unique_list)):
        print(unique_list[i])