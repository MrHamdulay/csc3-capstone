#sheldon kisten
#List of names
#21 April 2014

print("Enter strings (end with DONE):")

x= True
name= []
while x:
    y= input()
    if y=="DONE":break 
    name.append(y)
    
print()

print("Right-aligned list:")

max=(max(len(x) for x in name))
for j in name:
    print(' ' * (max-len(j))+j)