uList = []
check_list = []

strings = input("Enter strings (end with DONE):\n")     

while strings.upper() != 'DONE':
    uList.append(strings)
    strings = input("")    

print("\nUnique list:")       
for i in range(len(uList)):
    if uList[i] in check_list:
        continue
    else:
        check_list.append(uList[i])
        print(uList[i])        
        

    