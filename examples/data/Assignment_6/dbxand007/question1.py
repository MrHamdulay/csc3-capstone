"""Cherise Dube
19 April 2014
Program to print out a list of strings"""

strings=input("Enter strings (end with DONE):\n")
string_list=[]
if strings=='DONE':
    print()
    print("Right-aligned list:")
    
else:
    while strings != "DONE":
        string_list.append(strings)
        strings=input("")
    
#Finds the length of each string and creates a string of the lengths
    len_list_items=[]
    for i in string_list:
        length=len(i)
        len_list_items.append(length)
        
    
#Prints a right-aligned list according to the longest string    
    longest_string= max(len_list_items) 
    print()
    print("Right-aligned list:")
    for j in string_list:
        space=longest_string-len(j)
        print(" "*space,j,sep="")
        
    

    