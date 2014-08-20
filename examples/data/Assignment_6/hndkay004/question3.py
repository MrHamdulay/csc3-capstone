#program to count number of votes for each political party
#Kayla Hendricks
#23 April 2014

def elections():
    print("Independent Electoral Commission")
    print("--------------------------------")
    #starting with two empty lists
    party_list = []
    rep_list = []
    party = input("Enter the names of parties (terminated by DONE):\n")
    
    while party != "DONE":
        #adding user's input into first list 
        party_list.append(party)
        party=input()
    print("\nVote counts:")
    
    for i in party_list:
        #if items in first list exists in second list, loop again. 
        if i in rep_list:
            continue
        #if not, add item to second list
        else:
            rep_list.append(i)
            
    x=0
    for i in rep_list:
        #sort second list into alphabetical order and get counters of items in first list
        rep_list.sort()
        print("{0:10} - {1}".format(rep_list[x],party_list.count(rep_list[x])))
        x+=1
        
elections()
    
