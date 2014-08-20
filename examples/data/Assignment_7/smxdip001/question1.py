#question1
#Author: Dipanjali Samoo
#Student Number: SMXDIP001

print("Enter strings (end with DONE):")
in_list= input("") #this will prompt user for input
array= [in_list]
#this will sort input into list
while in_list!="DONE":
    in_list=input("")
    array.append(in_list)
while in_list=="DONE":
    break
len_array=len(array)
array= array[0:(len_array-1)]
dup= array*1
dup.reverse()
#this loop will help remove duplicates from the list
for i in dup:
    while dup.count(i)>1:
        dup.remove(i)
dup.reverse()
print("\n""Unique list:")
for i in dup:
    print(i)