#code to enter in marks and produce a histogram of those marks. Joshua Michelson 22/01/2014#
listofgrades = input("Enter a space-separated list of marks:\n").split(" ")
count0f1 = 0
count0f2p = 0
count0f2m = 0
count0f3 = 0
count0ff = 0
for i in listofgrades:
    if int(i) >= 75:
        count0f1 += 1
    elif int(i) >= 70:
        count0f2p += 1
    elif int(i) >= 60:
        count0f2m += 1 
    elif int(i) >= 50:
        count0f3 += 1
    else:
        count0ff += 1
print("1 |" +"X"*count0f1)
print("2+|" +"X"*count0f2p)
print("2-|" +"X"*count0f2m)
print("3 |" +"X"*count0f3)
print("F |" +"X"*count0ff)