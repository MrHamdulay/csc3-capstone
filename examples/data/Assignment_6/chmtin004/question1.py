'''Program to format a list of names
Tinotenda Chevmura (CHMTIN004)
20 April 2014'''

#create empty list
#retrieve names from the user

names = []
name = input("Enter strings (end with DONE):\n")

if name != "DONE":
    names.append(name)
    while name != "DONE":
        name = input()
        names.append(name)
 
#remove the "DONE" from the list

if len(names) > 1:
    del names[len(names)-1]

#print the right justified list

print("\nRight-aligned list:")

#look for the longest string in the list
    
length = 0
for nym1 in names:
    if len(nym1) > length:
        length = len(nym1)
    
    #Print the right alligned list
    
for zita in names:
    length = str(length)
    form = "{0:>"+length+"}"
    zita = form.format(zita)
    print(zita)
        
#______________________Program Ends Here_______________________