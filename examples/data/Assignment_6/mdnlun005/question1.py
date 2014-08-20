"""program  where the user can enter a list of strings followed by the
sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string
Lungelo Mdunge
21 April 2014"""


"Get input"
namelist = []
name = input("Enter strings (end with DONE):\n")
while name != "DONE":
    namelist.append(name)
    name=input('')

if namelist:
    namelength=[]
    for i in namelist:
        namelength.append(len(i))
    width=max(namelength)
print()
print("Right-aligned list:")
for name in namelist:
    if name=="DONE": break
    print(name.rjust(width))
