#strings...
#Joshua Hewitson
#4/16/2014

length = 0

x = input("Enter strings (end with DONE):\n")
print("")
mylist = []

while x != "DONE":
    mylist.append(x)
    if len(x) > length:
        length = len(x)
    x = input("")
    
print("Right-aligned list:")
for i in range(len(mylist)):
    print(str('{:>' + str(length) + '}').format(mylist[i]))