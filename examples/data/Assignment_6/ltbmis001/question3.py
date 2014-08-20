print("Independent Electoral Commission")
print("--------------------------------")
p=input("Enter the names of parties (terminated by DONE):\n")

a=0
names=[p]
    
if p!="DONE":
    while a!='DONE':
        a=input("")
        names.append(a)

    
new = names[0:(len(names)-1)]
n=[]
c=[]
q=a
while new!=[]:
    if new[0] not in n:
        n.append(new[0])
        p=(new.count(new[0]))
        c.append(str(p))
    if new[0] in n:
        del new[0]
        
g=[]    
for i in range(len(n)):
    g.append([n[i],c[i]])

print("\nVote counts:")

g=sorted(g)

for i in g:
        print(i[0]+" "*(11-len(i[0]))+"- "+i[1])
