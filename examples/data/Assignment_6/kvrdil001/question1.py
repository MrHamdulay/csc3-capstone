#Dilan Koovarjee
#List of names
#20 April 2014

print("Enter strings (end with DONE):")

i= True
name_list= []
while i:
    x= input()
    if x=="DONE":break 
    name_list.append(x)
    
print()

print("Right-aligned list:")

hat=(max(len(i) for i in name_list))
for j in name_list:
    print(' ' * (hat-len(j))+j)