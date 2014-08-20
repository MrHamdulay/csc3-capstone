x=['']
print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
while x[-1]!="DONE":
     x.append(input())
print("Vote counts:")
x.sort()
x.remove("DONE")
x.append(" ")
for i in range(1,len(x)-1,1):
     if x[i]!=x[i+1]:
          print(x[i].ljust(11)+"-",x.count(x[i]))
         