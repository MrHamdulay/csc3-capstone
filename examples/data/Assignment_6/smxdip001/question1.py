#program about lists and dictionaries
#question1
#Author:Dipanjali Samoo
#Student Number:SMXDIP001
array= []
print("Enter strings (end with DONE): \n")
strings="" #will prompt the user to input strings
#a loop used to populate the lists with strings
while strings!="DONE":
    strings= input("")
    array.append(strings)
while strings=="DONE":
    break
d=len(array)
array=array[:d-1]

if d!=1 and array[0]!="DONE":
    duplicate_array= array*1
    duplicate_array.sort(key=len)
    longest_string= duplicate_array[-1]
    longest_length= len(longest_string)
print("Right-aligned list: ")

#loop to print and align the strings in list
for i in (array):
    sp= ((longest_length)-len(i))*" "
    print(sp+i)
    