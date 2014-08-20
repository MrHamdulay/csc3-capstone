x=input("Enter strings (end with DONE):\n")
list1=[]
list1.append(x)
while x!= "DONE":
    x=input()
    list1.append(x)
    
del list1[len(list1)-1]
 
list1=" ".join(list1)

def search(l):
    newlist = []
    [newlist.append(x) for x in l if x not in newlist]
    return newlist

a=list1
a=" ".join(search(a.split()))


a=a.split(" ")
print()
print("Unique list:\n",end="")
for i in range(len(a)):
    print(a[i])
