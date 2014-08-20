"""Remove duplicates from list of inputs
Christopher Sterley
27/04/2014"""

#get first string input
str_for_list=input("Enter strings (end with DONE):\n")

#creat list variable to add unique words to
unique_list=[]

#continue to get inputs until DONE
while str_for_list!="DONE":
    if not str_for_list in unique_list:
        unique_list.append(str_for_list)
    str_for_list=input("")

print()
print("Unique list:")

#print out answer    
for i in range (len(unique_list)):
    print(unique_list[i])