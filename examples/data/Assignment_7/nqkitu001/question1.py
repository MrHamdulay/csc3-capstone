"""ASsignment 7 Question 1
Itumeleng Nqoko
27th April 2014"""

#This program prints out a list of strings in the same order, without any duplicates
lis=[]
strings=input("Enter strings (end with DONE):\n")
while strings!="DONE":
    if strings not in lis:
        lis.append(strings)
        strings=input("")
    if strings in lis:
        strings=input("")
print("")
print("Unique list:")
for strings in lis:
    print(strings)
