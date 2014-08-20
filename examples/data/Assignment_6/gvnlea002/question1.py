"""Leandra Govender
list of strings aligned right to longest string
21 April 2014"""

print("Enter strings (end with DONE):")

i= True
name_list= []
while i:
    x= input()                                       #loop stops when Done is entered
    if x=="DONE":break 
    name_list.append(x)
    
print()

print("Right-aligned list:")

if name_list==[]:
    print()
else:
    y=(max(len(i) for i in name_list))
    for l in name_list:
        print(' ' * (y-len(l))+l)
        
        
    
    