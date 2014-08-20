listing = []
listee = input("Enter strings (end with DONE):\n")

while listee != "DONE":
    listing.append(listee)
    listee = input("")



new_list = []

def deleting(listing):
    counting = []
    i = 0
    if len(listing) == 0:
        return new_list
        
    else:
        for i in range(1, len(listing)):
            if listing[0] == listing[i]:
                adding = str(i)
                counting.append(adding)
                
            else:
                continue
        for i in range(len(counting)):
            evaled = eval(counting[i])
            del listing[evaled-i]
            i += 1
        
        new_list.append(listing[0])
        del listing[0]
        
        deleting(listing)
        
        return new_list

x = deleting(listing)

print()
print("Unique list:")
for i in range(len(new_list)):
    print(new_list[i])
    