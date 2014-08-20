#ashton

wlist = []


w = input("Enter strings (end with DONE):\n")
while w.lower() != "done":
    if not w in wlist: #
        wlist.append(w) 
    w = input()
    

print("\nUnique list:")
for w in wlist:
    print(w)
    