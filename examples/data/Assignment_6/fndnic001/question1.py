'''Program to make a list of names right alligned
nic findlay
21 april 2014'''

names = []
name = ('')
print("Enter strings (end with DONE):")

while name != 'DONE': #loop to enter names
    name = input('')
    names.append(name)

del names[len(names)-1]  #deletes 'DONE' from loop

max_name = max(names, key = len)

print("\nRight-aligned list:")
for i in names:                                #right alligning words
    print((len(max_name) - len(i)) * ' ' + i)