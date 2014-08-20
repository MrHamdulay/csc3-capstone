be = True
print("Enter strings (end with DONE):")
list = []
longword = 0
while be == True:
    temp = input()
    if temp == 'DONE':
        break
    if len(temp)>longword:
        longword = len(temp)
    list.append(temp)
print("\nRight-aligned list:")
for z in list:
    t = (longword-len(z))
    print(" " * t,z,sep='')