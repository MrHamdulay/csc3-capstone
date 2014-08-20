# a program to count the number of votes for each political party in an election
# Budeli Rendani
# BDLREN001
# 20/04/2014

z=[] # Creating an empty list for storing the names of the parties
def main():
    global z # Bringing the list into the function
    print("Independent Electoral Commission")
    print("--------------------------------")
    
    x=input("Enter the names of parties (terminated by DONE):\n") # Obtaining input from the user
    z.append(x) # Adding the input to the empty list
    while x != "DONE":
        x=input() # Obtaining input from the user
        z.append(x) # Adding the input to the empty list
    c=len(z) # Finding the number of strings in the  list in order to delete the word DONE from the list
    del z[c-1] # Deleting the word DONE from the list
    
    # Looping through the list to build a count dictionary
    counts={}
    for i in z:
        counts[i]=counts.get(i,0) +1 
    parties=list(counts.keys()) # Getting a list of the party names
    parties.sort() # Putting the words in alphabetical order
    print("\nVote counts:")
    
    # Printing out the words with the associated count
    for i in parties:
        u=9
        v=len(i)
        m=u-v # Spacing between the name and the count
        print(i,m*" ","-",counts[i])
        
        
main()