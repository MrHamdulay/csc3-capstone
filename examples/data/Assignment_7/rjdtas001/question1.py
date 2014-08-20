names=[]
vote=input("Enter strings (end with DONE):\n")
while vote != "DONE":
    names.append(vote)
    vote=input("")

ballot=[]
for vote in names:
    if vote not in ballot:
        ballot.append(vote)

print()
print("Unique list:")
for i in ballot:
    print(i)
