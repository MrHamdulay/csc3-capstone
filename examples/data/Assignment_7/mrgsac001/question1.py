"""Aligning strings
Sachin Murugan
24/04/2014"""
list1 = []
strings = input("Enter strings (end with DONE): \n")
#Create a list of strings
while strings != "DONE":
    list1.append(strings)
    strings = input("")

print()
print ("Unique list:")
#create another list for which no duplicates will be appended
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i) 
    else:
        pass
for i in list2:
    print(i)
        