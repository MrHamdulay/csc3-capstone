''' program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates
Lungelo Mdunge
28 April 2014'''


"Get input"
namelist = []
name = input("Enter strings (end with DONE):\n")
while name != "DONE":
    if name not in namelist:
        namelist.append(name)
    name=input('')
print()
print("Unique list:")
for i in namelist:
    print(i)