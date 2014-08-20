""""Ogone Molefe MLFOGO001
Assignment 7_Question """

print("Enter strings (end with DONE):")
in_list=input("") #prompt user for input
array=[in_list]
#sort input into list
while in_list!="DONE":
    in_list=input("")
    array.append(in_list)
while in_list=="DONE":
    break
len_array=len(array)
array= array[0:(len_array-1)]
duplicate= array*1
duplicate.reverse()
#loop to remove duplicates from list
for i in duplicate:
    while duplicate.count(i)>1:
        duplicate.remove(i)
duplicate.reverse()
print("\n""Unique list:")
for i in duplicate:
    print(i)
    
    

    
