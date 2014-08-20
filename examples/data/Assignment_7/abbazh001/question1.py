#Azhar Aboobaker
#ABBAZH001
#28/04/2014

def string():
    strings=[]
    print("Enter strings (end with DONE):")
    x=input()
    while x!="DONE":
        strings.append(x)
        while x:
            x=input()
            if x=="DONE":
                break
            strings.append(x)
    return strings

def uniquelist():
    strings=[]
    for i in string():
        if i not in strings:
            strings.append(i)
    print()        
    print("Unique list:")
    for j in strings:
        print(j)

uniquelist()