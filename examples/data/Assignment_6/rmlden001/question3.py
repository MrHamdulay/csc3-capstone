#DenishaRamaloo
#Studentnumber:RMLDEN001

print("Independent Electoral Commission")
print("--------------------------------")
names=[]
name=input("Enter the names of parties (terminated by DONE):\n")
while name!="DONE":
    names.append(name)
    name=input("")

count = {}
    

for word in names:
    if not word in count:
        count[word] = 1
    else:
        count[word] += 1
some = list()
for j in names:
   
    if j not in some:
        some.append(j)

some.sort()

print('\nVote counts:')

for i in some:
    y = 11-len(i)
    print ( i,' '*y+'- ',count[i],sep='')
    
    