print("Independent Electoral Commission\n--------------------------------")
enter = input("Enter the names of parties (terminated by DONE):\n")

vote = [ ]

while (enter != "DONE"):
    vote.append(enter)    
    enter = input()


p=[]


for i in range (len(vote)):
    if(vote.index(vote[i])==i):
        p.append(vote[i]) 


p.sort()        
c=[]
k=0


while(k<len(p)):
    k=k+1
    c.append(0)

for i in range(len(p)):
    for j in range(len(vote)):
        if(p[i]==vote[j]):
            c[i]+=1
            
print()
print("Vote counts:")

for i in range(len(p)):
    print("{0:<10} - {1}".format(p[i],c[i]))
    
