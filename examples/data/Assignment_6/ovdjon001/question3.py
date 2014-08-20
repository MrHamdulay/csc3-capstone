"""question 3 
20 April 2014
by Jonathan Ovadia"""
def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    votes = []
    line = input("")
    while line !="DONE":
        votes.append(line)
        line = input("")
    else:
        print("\nVote counts:")
        print(count(votes))

def count(l):
    output = ""
    parties = []
    dictionary = {}
    for i in range(len(l)):
        if l[i] not in parties:
            parties.append(l[i])
    votes = [0]*len(parties)    
    for i in range(len(parties)):
        for j in range(len(l)):
            if parties[i] == l[j]:
                votes[i] +=1
    #arrange in alphabetical order 
    for i in range(len(parties)):
        dictionary.update({parties[i]: votes[i]})
    for key, value in sorted(dictionary.items()): 
        output+= key + " "*(11-len(key)) + "- "+ str(value) + "\n"
    return output
main()