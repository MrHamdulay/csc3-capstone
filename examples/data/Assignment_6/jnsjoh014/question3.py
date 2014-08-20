"""Assignment 6 Question 3
Johan Jansen van Vuuren (JNSJOH014)
21 April 2014"""

def main():
    print("Independent Electoral Commission\n--------------------------------")
    parties = {}
    party = input("Enter the names of parties (terminated by DONE):\n")
    while party.upper()!="DONE":
        if party not in parties:
            parties[party] = 1
        else:
            parties[party]+=1
        party = input("")
    print("\nVote counts:")
    #print(parties)
    sorted_parties = sorted(parties)
    for i in range(len(sorted_parties)):
        formatString = "{0:<10}"
        tempString = formatString.format(sorted_parties[i])
        print(tempString,"-",parties[sorted_parties[i]])

if __name__=="__main__": main()