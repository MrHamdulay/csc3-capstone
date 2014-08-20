"""Assignnment 7 Question1
prints out a list in the same order without duplicates
Shaheen Karodia
KRDSHA003
2014-04-27"""

print("Enter strings (end with DONE):")


#initialise variables
string=""
list=[]
list_check=[]

#get input strings from user, append them to list, and break from loop when user inputs DONE
while string !=("DONE"):
    string=input("")
    if string !=("DONE"):
        list.append(string)
print()
print("Unique list:")


for i in list:
    if i not in list_check:     #check if item in list is in the check list #only prints those items that have not yet been added to list_check
        list_check.append(i)     #update list_check
        print(i)




