""" printing a list of strings with no duplicates
leandra govender
27 april 2014"""
strings=[]                                                 #create empty list
string= input("Enter strings (end with DONE):\n")          #ask for input
while string != "DONE":                                    #while input is not equal to DONE continue asking
    strings.append(string)                                 # add each input to the list
    string=input("")
    
unique_list=[]                                              #create a new list
for i in strings:
    if i not in unique_list:                                # adds items from old list to new list if not in the new list
        unique_list.append(i)                               
    else:
        pass                                                # if item is in the new list the repeted item is not added
print()
print("Unique list:")

for i in unique_list:
    print(i)                                               #prints the new list
    
