''' Yongama Giwu
30 April 2014
Program to remove duplcates in strings'''


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