'''program for ordered list without duplicates
nicole henning
due 2 may 2014'''

strings_list = []

strings = input("Enter strings (end with DONE):\n")
while strings != "DONE": #DONE acts as sentinel
    strings_list.append(strings) #add each string to existing list
    strings = input("")
    
print()

print("Unique list:")
    
duplicates = []
#print string only if not duplicated
for i in strings_list:
    if i not in duplicates: #restricts printing string only if uniique, ie not duplicated
        duplicates.append(i)
        print(i)