#Aceepting a list and right alligning it
#Keanon Fell
#24 April 2014

value =""
stringList= []

print("Enter strings (end with DONE):")

while (value != 'DONE'):
    value = input()
    if value != 'DONE':
        stringList.append(value)
    
maximum =0    
for i in range(len(stringList)):
    if len(stringList[i]) > maximum:
        maximum = len(stringList[i])
print()        
print("Right-aligned list:")
for j in range(len(stringList)):
    spacing = maximum - len(stringList[j])
    print(spacing * " ",stringList[j],sep="")