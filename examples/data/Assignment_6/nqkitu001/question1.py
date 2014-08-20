"""Assignment 6 question 1
Itumeleng Nqoko
April 24 2014"""
lis=[]
strings=input("Enter strings (end with DONE):\n")
while strings!="DONE":
 lis.append(strings)
 strings=input("")

print("\nRight-aligned list:")
max= 0
for j in lis:
 if len(j)>=max:
  max=len(j)
for i in lis:
 aligned=("{0:>"+str(max)+"}").format(i)
 print(aligned)
