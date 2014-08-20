#Azhar Aboobaker
#ABBAZH001
#23/04/2014

def parties():
    y=[]
    print("Enter the names of parties (terminated by DONE):")
    x=input()
    if x!= "DONE":
        y.append(x)
        while y:
            x=input()
            if x=="DONE":
                break
            y.append(x)
    return y

def votecounts():
    print("Independent Electoral Commission")
    print("-"*32)
    a=parties()
    b=[]
    for i in a:
        if i in b:
            continue
        b.append(i)
    b=sorted(b)
    print()
    print("Vote counts:")
    for j in b:
        print(j.ljust(10), "-", a.count(j))
        
votecounts()