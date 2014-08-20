"""Enter strings delete duplicates print"""
#Liam Brodie
#BRDLIA004
#April 2014

print("Enter strings (end with DONE):")
mainlist = []
i = ""
while i != "DONE":
    i=input("")
    if i == "DONE":
        break
    else:
        mainlist.append(i)
      
uniquelist = []

for j in mainlist:
    if j in mainlist and j not in uniquelist:
        uniquelist.append(j)

print()

print("Unique list:")
for l in uniquelist:
    print(l)