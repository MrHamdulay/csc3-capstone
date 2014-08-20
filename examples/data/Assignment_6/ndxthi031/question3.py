"""voting program
Thiolan Prevan Naidoo
NDXTHI031
25 april 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

names=[]
nameX=input("Enter the names of parties (terminated by DONE):\n")
while nameX!="DONE":
    names.append(nameX)
    nameX=input("")

count = {}#initialises a dictionary
    

for vote in names:
    if not vote in count:
        count[vote] = 1
    else:
        count[vote] += 1
new = list()
for i in names:
   
    if i not in new:
        new.append(i)

new.sort()

print('\nVote counts:')

for j in new:
    print ( j,' '*(11-len(j))+'- ',count[j],sep='')
    
    