"""Kekolo Phetla
PHTKEK001
Assignment 6 Question 1
21 April 2014"""

#get list of strings from user
liststring=[]
string_list=input("Enter strings (end with DONE):\n")
while string_list != "DONE":
    liststring.append(string_list)
    string_list=input("")
    
#find longest string in list
mAx=''
for string in liststring:
    if len(mAx)<len(string):
        mAx=string
print('')
print("Right-aligned list:")

#output right-aligned list
for string in liststring:
    space=len(mAx)-len(string)
    print(' '*space,string,sep='')

    


    


