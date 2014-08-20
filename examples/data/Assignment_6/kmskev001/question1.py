"""program that prints names in a list that is right aligned 
   kevin kumasamba
   22 april 2014"""

#making a list and then appending each name given 
names=[]
length=[]
name=input("Enter strings (end with DONE):\n")
while name!="DONE":
    l=len(name)
    length.append(l)
    names.append(name)
    name=input("")

#printing the names
print("\nRight-aligned list:")
for n in names:
    maxl=max(length)
    new_n="{0:>{1}}".format(n, maxl)
    print(new_n)