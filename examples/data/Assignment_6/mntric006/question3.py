print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
newstring = ""
lstparties = []
lstvotes = []
while newstring != "DONE":
    newstring = input()
    new = True
    posold = -1
    for i in range(len(lstparties)):
        if newstring == lstparties[i]:
            new = False
            posold = i
    if new == True:
        lstparties.append(newstring)
        lstvotes.append(1)
    else :
        lstvotes[posold] += 1

lstparties.pop()
for j in range(len(lstparties)):
    lstparties[j] += str(lstvotes[j])

lstparties.sort()
print(" ")
print("Vote counts:")
for k in range(len(lstparties)):
    party = lstparties[k]
    print(party[:-1] + " "*(11-len(party)) + " - " + party[-1])