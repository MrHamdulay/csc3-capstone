#A program to count the number of votes for each political party in an election
#Author: Michelle Njoroge
#24 April 2014

def main():
    string1="Independent Electoral Commission"
    print(string1)
    print("-"*len(string1))
    party=input("Enter the names of parties (terminated by DONE):\n")
    
    parties=[]
    
    while party!="DONE":
        parties.append(party)
        party=input()
    
    parties.sort()
    dictionary={}
    
    for i in parties:
        if i not in dictionary:
            dictionary[i]=1
        else:
            dictionary[i]+=1
    
    print()
    print("Vote counts:")
    
    for party in dictionary:
        print(party.ljust(10), "-",dictionary[party])
main()

    
    
    