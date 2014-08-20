#Format List
#Sofia Palmer
#24 April 2014

name = input("Enter strings (end with DONE):\n")
names = []
max_len = 0
while name != "DONE":
    if (len(name) > max_len):
        max_len = len(name)
    names.append(name)
    name = input()
print() 
print("Right-aligned list:")   
for i in range(len(names)):
    print(names[i].rjust(max_len))
