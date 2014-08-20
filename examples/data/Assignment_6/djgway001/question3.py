#adding up and displaying votes alphabetically
#wayne de jager
#24 april 2014

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

#creates list of names of parties
votelist=[]
while True:
    a=input()
    if a=="DONE":
        break
    else:
        votelist.append(a)

cleanlist=set(votelist) #removes duplicates, returns in a set format, not a list
displaylist=sorted(cleanlist) #orders parties alphabetically, 'sorted' converts set to list

#counting of votes in votelist
numofvotes=[]
for i in range(0,len(displaylist)):
    tally=votelist.count(displaylist[i])
    numofvotes.append(tally)
    
#display outcome
print()
print("Vote counts:")
for i in range(0,len(displaylist)):
    print("{0:<{1}}".format(displaylist[i],10),"-",numofvotes[i]) #left alligns the parties in 10-character space
