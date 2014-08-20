'''NDXMIC014
30 April 2014'''

print("Enter strings (end with DONE):")
string=[]
vote=""

while(vote!="DONE"):
    vote=input()
    string.append(vote)
string.remove("DONE")
cnt=0
rev=[]
for i in range(len(string)):
    if(string.index(string[i])==i):
        rev.append(string[i])
  

print()
print("Unique list:")
for i in range(len(rev)):
    print(rev[i])