# question3.py
# a program to count the number of votes for 
# each political party in an election
# Thomas Konigkramer
# 23 April 2014

def voting():
    
    print("Independent Electoral Commission\n"
          "--------------------------------")
    
    # empty dictionary
    counter = {}
    
    # asks for input from user
    names = input("Enter the names of parties (terminated by DONE):\n")
    if names != "DONE":
        votes = [names]
    else:
        votes = []
    # enters first party entry into list
    # input asked continuously until DONE entered
    while names != "DONE":
        names = input()
        if names!= "DONE": # so that DONE is not added to list
            votes.append(names)
            
    # enters entries into dictionary
    for party in votes:
        if party not in counter:
            counter[party] = 0
        counter[party] += 1
    
    # creating sequence of tuples in alphabetical order
    alphabetical = sorted(counter.items()) 
    
    print()
    print("Vote counts:")
    number = 0
    for party in alphabetical:
        print("{0:<10}".format(alphabetical[number][0]), "-", alphabetical[number][1])
        number += 1
    
    # alphabetical[number][0]: accesses the numberth tuple's 1st value (party name)
    # alphabetical[number][1]: accesses the numberth tuple's 2nd value (frequency)

if __name__ == "__main__":
    voting()