"""A program that takes a list of strings and then prints out right-aligned with the longest string
Tafadzwa Moyo
21 April 2014"""



#Gets the list of strings
print("Enter strings (end with DONE):")
a=input()
strlist=[] #empty array
while a!="DONE":
    strlist.append(a)
    a=input()

#Gets the length of the longest string
maxlen=0
for i in strlist:
    if len(i)>maxlen:
        maxlen=len(i)

#Prints out the list of string right-aligned with the longest string
print()
print("Right-aligned list:")
for i in strlist:
    gap=maxlen-len(i)
    print(" "*gap+i)
    