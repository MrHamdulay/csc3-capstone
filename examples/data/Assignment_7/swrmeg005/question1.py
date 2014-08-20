# Megan Swartz
# SWRMEG005
# Assignment 7-Qustion 1

print("Enter strings (end with DONE):")
in_list=input("") #prompt input
array=[in_list]
while in_list!="DONE": #sort into list
    in_list=input("")
    array.append(in_list)
while in_list=="DONE":
    break
len_array=len(array)
array= array[0:(len_array-1)]
duplicate= array*1
duplicate.reverse()
for i in duplicate: #Loop
    while duplicate.count(i)>1:
        duplicate.remove(i)
duplicate.reverse()
print("\n""Unique list:")
for i in duplicate:
    print(i)
    
    

    
