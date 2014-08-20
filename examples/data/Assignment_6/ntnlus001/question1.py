"""program to type str and write them alligned from the right
Dr Luci Ntanjna
22 April 2014"""

a=[]
x=input("Enter strings (end with DONE):\n")
a.append(x)
y=0
while x!="DONE":
    if y<len(x):
        y=len(x)
    x=input("")
    a.append(x)


print("\nRight-aligned list:")   
for n in range(len(a)-1):
    print(a[n].rjust(y))