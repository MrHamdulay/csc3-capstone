# Matthew Finlayson - FNLMAT001 
# Assignment 6 question 3
# 22/04/14

print("Independent Electoral Commission")
print("--------------------------------")

s = input("Enter the names of parties (terminated by DONE):\n")

parties = [] # parties will become a 2d array, parties[0] is a list of the names of the parties and parties[1] is a list of the votes for each party

empty = True # if parties is empty it is true
while s != "DONE":
    if not empty and s in parties[0]: # if the party is in the list parties[0]
        index = parties[0].index(s) # gets index of the party 
        parties[1][index] += 1 # adds one vote to the corresponding party's votes number
    else: 
        if empty: # if the list is empty, it creates the list for the party names and the party votes
            parties.append([s])
            parties.append([1])
            empty = False
        else: # if the list is not empty and the party is not in the list, it adds it to the list and assigns it a vote of 1 
            parties[0].append(s) 
            parties[1].append(1)    
        
    s = input("")

print()

print("Vote counts:")

sortedList = []
def sort(parties):
    
    # sorts the list parties[0] to put them in alphabetic order and as it does so it makes sure each corresponding number of votes is also changed to the same new index value
    for i in range(len(parties[0])):
        maxValue = "zzzz"
        maxIndex = 0 # keeps track of the index of the value that is highest (closest to aaaa)
        for j in range(len(parties[0])):
            if parties[0][j] < maxValue:
                maxValue = parties[0][j]
                maxIndex = j
                
        sortedList.append(parties[0][maxIndex]+str(parties[1][maxIndex]))
        output = "{0:<11}- {1:<0}"
        print(output.format(parties[0][maxIndex], str(parties[1][maxIndex]))) # prints out the name of the party and the votes of the party in a nice format
        
        parties[0].remove(parties[0][maxIndex]) # removes the highest values so that the next highest values can be obtained in the next iteration of the sorting loop
        parties[1].remove(parties[1][maxIndex])

if not empty: # only sorts the list - parties - if the list is not empty
    sort(parties)