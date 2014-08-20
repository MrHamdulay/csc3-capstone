
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
name=[]
party=input()
if party != "DONE":
    name.append(party)
while party != "DONE":
    party=input()
    if party != "DONE":
        name.append(party)
print()
print("Vote counts:")
for x in sorted(set(name)):
    if len(x)<=10:
        y=10-len(x)
        space=" " * y

    print(x + space,"-",name.count(x))
    
    

    
    