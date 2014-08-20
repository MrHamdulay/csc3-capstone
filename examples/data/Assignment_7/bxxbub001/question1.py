#B.Booi list no duplicates

def nodup ():
    print("Enter strings (end with DONE):")
    list_of_names = []
    newlist = []
    Dic = {}
    i = 0
    name = ""
    while True:
        if name == "DONE":
            break
        else:
            name = input("")
            list_of_names.append(name)
            i+=1
    
    x=0
    while x != i:
        if list_of_names[x] in newlist:
            x+=1
        else:
            newlist.append(list_of_names[x])
    
    print()
    print("Unique list:")
    for j in range(len(newlist)-1):
        print(newlist[j])
            
nodup()