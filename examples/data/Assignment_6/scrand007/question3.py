print("Independent Electoral Commission\n--------------------------------")

string = input("Enter the names of parties (terminated by DONE):\n")
list_1 = [string]

if string == "DONE":
    print()
    print("Vote counts:")
    pass
else:
    while string != "DONE":
        string = input()
        if string == "DONE":
            break
        else:
            list_1.append(string)        
    list_2 = sorted(list_1)        
    new = (dict(zip(sorted(list_2),map(list_2.count,sorted(list_2)))))
    print()
    print("Vote counts:")
    t = 0
    for k, v in sorted(new.items()):
        print(k,' '*(9-len(k)),"-", v)