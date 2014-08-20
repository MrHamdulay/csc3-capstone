""" Program to count votes
Micaela Narasmulu
25 April 2014 """

print("Independent Electoral Commission")

print("--------------------------------")

v=[]

vote=input("Enter the names of parties (terminated by DONE):\n")

while vote !=  "DONE":
    v.append(vote)
    vote=input()
    
v.sort()
found=[]
f="{0:<10}"
print()
print("Vote counts:")


for  j in  v:
    if not j in found:
        w=v.count(j)
        print(f.format(j),"-",w)
        found.append(j)
        



