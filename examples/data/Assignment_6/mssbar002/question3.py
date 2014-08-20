"""a program to count the number of votes for each political party in an election
Barnett Msiska
23/04/2014"""
def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    parties = []
    party = input("Enter the names of parties (terminated by DONE):\n")
    while party != "DONE":
        parties.append(party)
        party = input("")
    partyList = {}
    for p in parties:
        if not p in partyList:
            partyList[p] = 1
        else:
            partyList[p] +=1
    print("\nVote counts:")
    for p in sorted(partyList):
        print(p + " "*(11 - len(p)) + "-", partyList[p])       
    
main()