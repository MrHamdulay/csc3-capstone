"""Programme for list without repitition
Julian Albert
ALBJUL005
29 April 2014"""

list_1 = [] #create list 
string = input('Enter strings (end with DONE):\n') #users input
list_1.append(string) #add to list
while string != 'DONE': 
    string = input('')
    list_1.append(string)
    
new_list = [] #create newlist
for x in list_1:
    if x not in new_list:
        new_list.append(x) #add each input in the old list to  the newlist

print()
print("Unique list:")        
for i in range(len(new_list)-1):
    print(new_list[i])