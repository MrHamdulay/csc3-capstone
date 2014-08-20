#Shivam Ragoonaden
#Program to right-align a list of words entered with the longest string


name = ""
count = 0
names = []
name = input("Enter strings (end with DONE):\n")
l = len(name) #To get the name with the highest length of characters

while name != "DONE":  #Sentinel
    names.append(name)  #Add to list of names
    count += 1  #Keep track of number of items in the list
    name = input("")
    if len(name) > l:  #Check if the name has a higher length than the current l
        l = len(name)

print()
print("Right-aligned list:")
        
for i in range(count):  #Go through the list
    space = l - len(names[i])  #Determine number of spaces for right-alignment
    print(" "*space + names[i])  