"""Voting count
Claudia Pastellides
23 April 2014"""

def vote():
    print("Independent Electoral Commission")
    print("--------------------------------")
    vote=input("Enter the names of parties (terminated by DONE):\n")
    print()
    list1=[] # finds first occurence
    list2=[] #checks for duplicates
    while vote!="DONE": #sentinal
        if vote not in list1: #if not a first occurance
            list1.append(vote) #add word to list one
        else:
            list2.append(vote) #already occurred, add to second
        vote=input() #continually gets input
    list1.sort() #alphabetical order
    print("Vote counts:")
    for i in list1: #first occurences
        count= list2.count(i) #counting how many times items in list 1 are also in list2
        print("{:<10}".format(i)+" -",count+1) # printing with format 
        #count add one so it includes appearance in list 1
        
    
vote()