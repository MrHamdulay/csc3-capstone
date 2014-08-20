'''A right-aligned list of a list given by a user
Author:Raees Eland
Date:19 April 2014'''

list=[]
print('Enter strings (end with DONE):')
string=input() # allows user to input strings
list.append(string)
while string!='DONE':
    string=input()
    list.append(string)
list.remove("DONE")#removes the string 'DONE' at the end of the list

# finds the string with the longest length
if list!=[]:
    len_str=0
    max_length=len(list[0])
    for i in list:
        len_str=len(i)
        if max_length<=len_str:
            max_length=len_str
    
print()
print('Right-aligned list:')
gap=0
for j in list:
    gap=max_length-len(j)
    print(' '*gap,j,sep='')
            
    
    