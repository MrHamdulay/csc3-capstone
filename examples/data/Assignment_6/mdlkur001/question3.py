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
for f in names:
   
    if f not in some:
        some.append(f)

some.sort()

print('\nVote counts:')

for i in some:
    z = 11-len(i)
    print ( i,' '*z+'- ',count[i],sep='')
    
    