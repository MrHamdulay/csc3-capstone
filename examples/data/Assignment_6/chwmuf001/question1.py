#Mufaro Chiwara - April 2014
#Get names and enter to list
name = input("Enter strings (end with DONE):\n")
list =[]
while name != 'done' and name!='DONE':
    list.append(name)
    name =input()

#Compare lengths of strings
lengths =[]
for i in list:
    lengths.append(len(i))
if lengths:
    gap=max(lengths)

#Print list
print()
print("Right-aligned list:")
for i in list:
    print(" "*(gap-len(i)),i,sep="")
    
    
    