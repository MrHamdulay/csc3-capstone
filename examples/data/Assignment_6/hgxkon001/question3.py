#Konrad Hugo
#question 3


#Function that gets names of parties and the subsequent votes for each party
def party_finder():
    listA = [] #
    string = '' #initially we want a blank string input, but we want a variable
    print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
    string = input()
    while string != "DONE":
        listA.append(string)
        string = input()
    
    return listA

#function counting the frequency of votes per party
def frequency_finder():
    listA = party_finder()
    listA.sort() #sort function
    listB = [] #list for checking whether vote has been counted already or not
    print("Vote counts:")
    for i in listA:
        if i not in listB:
            frequency = listA.count(i)
            listB.append(i) 
            vote_display = "{:<11}{}{}".format(i,"- ",frequency) #displays the vote count in required format
            print(vote_display)
        
frequency_finder()
