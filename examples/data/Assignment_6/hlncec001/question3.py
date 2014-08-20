print("""Independent Electoral Commission
--------------------------------""")
names = []
msg = input("Enter the names of parties (terminated by DONE):\n")
names.append(msg)

#print(names)

while msg != "DONE":
    msg = input("")
    names.append(msg)
    #print(names)
    
names.remove("DONE")
#print(names)

names.sort()
#print(names)

cnt = 1
num = 0
name_1 = ''
grp_names = []
for i in names:
    if name_1 != names[num]:
        name_1 = names[num]
        grp_names.append(name_1)
    else:
        cnt = cnt +1 
    num+=1
#print(grp_names)

letter = []
for x in grp_names:
    l = 0
    while x in names:
        names.remove(x)
        l +=1
    letter.append(l)
#print(letter)

r = 0
print()
print('Vote counts:')
for k in grp_names:
    print(grp_names[r]," "*(9-len(grp_names[r])),"-",letter[r])
    r+=1