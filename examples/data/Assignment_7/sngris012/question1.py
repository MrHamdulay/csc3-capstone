print("Enter strings (end with DONE):")
x=[]
a=""

while(a!="DONE"):
    a=input()
    x.append(a)
x.remove("DONE")
count=0
revised=[]
for i in range(len(x)):
    if(x.index(x[i])==i):
        revised.append(x[i])
  

print()
print("Unique list:")
for i in range(len(revised)):
    print(revised[i])