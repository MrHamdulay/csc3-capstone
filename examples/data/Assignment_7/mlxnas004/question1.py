"""nasha somoina meoli
27th april 2014
program to print unique items in a list"""
#get first item
item = input("Enter strings (end with DONE):\n")
items = [item]
unique_items = [item]
#get other items in list until done
while item != "DONE":
    item = input("")
    if item == "DONE":break
    #add unique items to a list 
    if item in items:
        continue
    else:
        unique_items.append(item)
    items.append(item)
#print the list of unique items
print()
print("Unique list:")
for i in unique_items:
    if i != "DONE":
        print(i)
    