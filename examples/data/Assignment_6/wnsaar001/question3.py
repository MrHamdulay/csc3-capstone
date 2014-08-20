"""voting program
Aaron Weinstein
23 April 2014"""


partys={}
#stores party names and assigns votes
def getparties(name):        
    if name =="DONE":
        return ""
    else:
        if name in partys:
            partys[name]= partys[name]+1
            name = input("")
            tot = getparties(name)
        else:
            partys[name] = 1
            name = input("")
            tot = getparties(name)
        return  partys
 #prints the votes formatted
def printparties(parties):
    if len(parties)==0:
        return 0
    else:
        partykey = list(parties.keys())
        valueofkeys = list(parties.values())
        partykey.sort()
        for i in range(len(partykey)):
            print(partykey[i]," "*(10-len(partykey[i]))," - ",parties[partykey[i]],sep='')
       
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
partiesname = input("")
parties = (getparties(partiesname))
print()
print("Vote counts:")
printparties(parties)