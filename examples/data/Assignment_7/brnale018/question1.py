# Program to get a list of strings and print the list without repreating a string.
# Alex Brunette
#01/05/14

get_list=input("Enter strings (end with DONE):\n") #get input
list_str=[] #empty list
while get_list != "DONE" :
    list_str.append(get_list) #add strings to list
    get_list=input('')

new_list=[] #create a new list
for i in list_str:
    if i in new_list: 
        continue #do not add string if string is already in list
    else:
        new_list.append(i) #add string to list if not already in list
        
print('')
print("Unique list:")
for j in new_list:
    print(j) #print list without repitions of strings
    
        
    
