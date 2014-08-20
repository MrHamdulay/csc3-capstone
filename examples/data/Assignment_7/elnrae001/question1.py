''' Program that prints a unique list from an inputed list
Author:Raees Eland
Date: 28 April 2014'''

string=input('Enter strings (end with DONE):\n')
list=[]
list.append(string)
while string!='DONE':
    string=input()
    list.append(string)
list.remove("DONE")
list.reverse() # reverse the list to remove the last occurrance of a string

print()
print('Unique list:')
for i in list:
    while list.count(i)>1:
        list.remove(i)
list.reverse() # reverse the list again to print it out in the order given

print('\n'.join(list))
        
