"""program to siort a given list into a list6 without duplicates
yasha longstaff
29 april 2014"""

item = input('Enter strings (end with DONE):\n')
full_list = []
if item != 'DONE':
    full_list = [item]
    
while item != 'DONE':
    item = input()
    if item != 'DONE':
        full_list.append(item)
        
unique_list = []
for i in range(len(full_list)):
    if not full_list[i] in unique_list:
        unique_list.append(full_list[i])
    else:
        pass
    #return unique_list

print()
print('Unique list:')
for j in unique_list:
    print (j)
  

