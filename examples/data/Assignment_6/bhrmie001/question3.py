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

def votes():
    print("Independent Electoral Commission")
    print("-"*32)
    z=parties()
    r=[]
    for i in z:
        if i in r:
            continue
        r.append(i)
    r=sorted(r)
    print()
    print("Vote counts:")
    
    for j in r:
        print(j.ljust(10), "-", z.count(j),)
        
votes()