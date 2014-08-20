def voting():
    
    repetition = {} # Creating an empty dictionary
    
    print("Independent Electoral Commission\n"
          "--------------------------------")
    
    candidates = input("Enter the names of parties (terminated by DONE):\n")
    votes = [candidates]
    
    # Asks for candidates and ends the list if DONE is and input
    while candidates != "DONE":
        candidates = input() # Always use an empty string for while loops when counting
        votes.append(candidates) # Adds the names to the list
    votes.remove("DONE") # Removes DONE from the list
    
    for party in votes:
        if party not in repetition:
            repetition[party] = 0 # Creating a new entry into the dictionery
        repetition[party] += 1 # Adding 1 for every repitition
    
    alphabetical = sorted(repetition.items())  
    
    print()
    print("Vote counts:")
    number = 0
    for party in alphabetical:
        print(alphabetical[number][0], (10 - len(alphabetical[number][0])) * " ", " ", "-", " ", alphabetical[number][1], sep = "")
        number += 1
    
voting()    