print("Independent Electoral Commission")
print("--------------------------------")
name = input("Enter the names of parties (terminated by DONE):\n")
NAMES = dict()
while name != "DONE":
    if name in NAMES.keys():
        NAMES[name] += 1
    else:
        NAMES[name] = 1
    name = input()
print()
print("Vote counts:")
for i in sorted(NAMES.keys()):
    print("{:10}".format(i),"-",NAMES[i])
