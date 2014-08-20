#Program to print a user's entered list in same order without duplicates
#Ethan Jackson
#28 April 2014

print("Enter strings (end with DONE):")
names =''
lis = []
while names != "DONE":
    names = input("")
    if names not in lis:
        lis.append(names)       #only adds the item to the list if it's the first occurence of that item
        #therefore it will never add a duplicate item
        
lis.remove("DONE")
print("\nUnique list:")
for i in lis:
    print(i)
    
    