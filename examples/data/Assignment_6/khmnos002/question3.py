"""program to count number of votes for each political party in elections
nosipho khumalo
19 April 2014"""

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    
    parties = [] #list will be created as names are encountered
    aparty = input("Enter the names of parties (terminated by DONE): \n")
    while aparty != "DONE":
        parties.append(aparty)
        aparty = input("")

    #creating counter for number of votes
    counter = {}
    for aparty in parties:
        if not aparty in counter:
            counter[aparty] = 0
        counter[aparty] += 1 
          
    parties.sort()    
    #printing number of votes for each party
    print("")
    print("Vote counts:")  
    for aparty in sorted(counter):
        print("{0:10} - {1}".format(aparty, counter[aparty])) 
main()