"""Aligning strings
Sachin Murugan
24/04/2014"""
list1 = []
strings = input("Enter strings (end with DONE): \n")
Max = 0
while strings.upper() != "DONE":
    list1.append(strings)
    MaxLen = len(strings)
    if Max < MaxLen:
        Max = MaxLen
    strings = input("")
print()
print ("Right-aligned list:")
allignment = "{0:>" + str(Max) + "}"
for i in list1:
    print(allignment.format(i))