lists = []

users_list = input("Enter strings (end with DONE):\n")

while users_list != "DONE":
    lists.append(users_list)
    users_list = input("")

lists2 = []

def delZ(lists):
    acc = []
    i = 0
    
    if len(lists) == 0:
        return lists2
        
    else:
        for i in range(1, len(lists)):
    
            if lists[0] == lists[i]:
                sums = str(i)
                acc.append(sums)
                
            else:
                continue

        for i in range(len(acc)):
            evaled = eval(acc[i])
            del lists[evaled-i]
            i += 1
        
        lists2.append(lists[0])
        del lists[0]
        
        delZ(lists)
        
        return lists2

x = delZ(lists)

print()
print("Unique list:")
for i in range(len(lists2)):
    print(lists2[i])