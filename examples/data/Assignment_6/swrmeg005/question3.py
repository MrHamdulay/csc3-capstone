#A program that allows us to count the number of votes received by each political party in an election and then printing them out in columnar format
#Megan Swartz
#24 April 2014

def election():
    
    #print intro message
    print("Independent Electoral Commission")
    print("--------------------------------")
    
    #start getting list of party names
    #initialize a list and add to list
    
    parties_list = []
    parties = input("Enter the names of parties (terminated by DONE):\n")
    
    while parties != "DONE":
        parties_list.append(parties)
        parties = input("")
    
    #find distinct parties and create a list with them in it
    
    list_distinct = []
    for i in parties_list:
        if not i in list_distinct:
            list_distinct.append(i)
        else:
            continue
    
    list_distinct.sort()
    
    #print out a list with the party names and number of votes
    print("\nVote counts:")
    for i in list_distinct:
        print(i.ljust(10), "-", parties_list.count(i)) 
    
election()