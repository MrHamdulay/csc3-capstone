#Program to right-align a list of strings
#Nkosi Gumede
#26 April 2014

listed= []
x=input("Enter strings (end with DONE):\n")
n=1
while x!="DONE":
    listed.append(x)
    if len(x)>n:
        y=len(x)
        n=y
    x=input("")
out="{0:>"+str(y)+"}"
print("")
print("Right-aligned list:")
for i in listed:
    print(out.format(i))