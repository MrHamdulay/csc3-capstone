#sheldon kisten
#List of names
#21 April 2014

print("Enter strings (end with DONE):")

i= True
name_list= []
while i:
    y= input()
    if y=="DONE":break 
    name_list.append(y)
    
print()

print("Right-aligned list:")

if len(name_list) != 0:
    max1=(max(len(i) for i in name_list))
    for j in name_list:
        print(' ' * (max1-len(j))+j)
