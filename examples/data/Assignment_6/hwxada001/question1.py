a = False
print("Enter strings (end with DONE):")
list = []
long = 0
while a == False:
    temp = input()
    if temp == 'DONE':
        break
    if len(temp)>long:
        long = len(temp)
    list.append(temp)
print("\nRight-aligned list:")
for z in list:
    t = (long-len(z))
    print(" " * t,z,sep='')