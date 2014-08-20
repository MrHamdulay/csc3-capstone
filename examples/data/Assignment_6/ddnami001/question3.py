#Amitha Doodnath
#DDNAMI001
#23/04/2014
#Programme to count votes for political parties

print("Independent Electoral Commission")
print("--------------------------------")

votes=[]

vote=input("Enter the names of parties (terminated by DONE):\n")

while vote != "DONE":
    votes.append(vote)
    vote=input()
    
votes.sort()
found=[]
f="{0:<10}"
print()
print("Vote counts:")

for i in votes:
    if not i in found:
        v=votes.count(i)
        print(f.format(i),"-",v)
        found.append(i)
        



