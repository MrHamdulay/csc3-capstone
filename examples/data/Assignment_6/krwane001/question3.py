print("Independent Electoral Commission")
print("--------------------------------")
p = []
p1 = input('Enter the names of parties (terminated by DONE):\n')
while p1 != "DONE":
    p.append(p1)
    p1 = input("")
print("")
p2 = []
p.sort()
print("Vote counts:")
for p1 in p:
    if not p1 in p2:
        p2.append(p1)
        print((p1),(p.count(p1)), sep="")

