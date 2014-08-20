print("Independent Electoral Commission\n--------------------------------")

def start():
    name = input("Enter the names of parties (terminated by DONE):\n")
    parties = [] #empty list for strings
   
    while name != "DONE":   # stops iterating when input = DONE    
        parties.append(name) # adds string onto list
        name = input()    # gets the next input
    print()
    print("Vote counts:")
    votes(parties)     # calls votes function sending all strings
    
def votes(parties):
    count = 1   # counter
    parties.sort() # sorts strings into alpha order
    for i in range(0,len(parties)-1): #iterates the number of str/blocks in the list
        if parties[i] == parties[i+1]:# checks to see whether the string is = to the next string in the list
            count += 1 #then the counter goes up by one
            if i == len(parties)-2: # makes sure that if the last string is = to the one before it then it will take it in to account
                print(parties[i]+ " " * spaces + "- ",count,sep = "")
            
        else:
            spaces = 10 - (len(parties[i])-1) # gets the num of spaces needed
            print(parties[i]+ " " * spaces + "- ",count,sep = "")
            count = 1 # sets count back to 1 so that the next strin in the list can be counted
            if i == len(parties)-2: # ensures that the last str is'nt left out
                spaces = 10 - (len(parties[i+1])-1)
                print(parties[i+1]+ " " * spaces + "- ",count,sep = "")            
    
start()# calls start