#MTHKHI001
#Assignment 6
#Question 3

# get user input, necessary, to occupy the first space of each array else, the while loop will not execute.
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
Partynames = [""]
votescounter = [0]

# user_input acts as a string "counter", as it temporarily holds the user input and transfers it to the array, so long as it is unique to the array.
User_Input = ""
while User_Input != "DONE":
    User_Input = input()
    flag = 0
    for i in range (len(Partynames)):
        # if input is unique append it to the names array, aswell as add a corresponding vote of 1 to the votes array, which will occupy the same position in its own array
        if Partynames[i] == User_Input:
            votescounter[i] = votescounter[i] + 1
            flag = 1
        # since the input is not unique, it is then instead tallied, to a numeric array, that corresponds with the list of names, so that votes in position 1 are related to the name in position one of the corresponding array
    if flag != 1:
        Partynames.append(User_Input)
        votescounter.append(1)

# now that the arrays have been filled, they will be useable in a loop, as previously without the input in the first position, the array would not have executed.it is now unnecessary to occupy the first position of the arrays
del Partynames[0]
del votescounter[0]
# used to delete the done, that would be appended to the arrays
del Partynames[(len(Partynames)-1)]
del votescounter[(len(votescounter)-1)]
 
    
print()
print("Vote counts:")
#creating a new array, based on the original names array, with the difference that it is a sorted version of it.
sortedPartynames = list(Partynames)
sortedPartynames.sort()

#counter
#used to determine, the shortest words, length, necessary for formatting further on
minimum = 0
for q in range (len(sortedPartynames)):
    if len(sortedPartynames[q]) < minimum:
        minimum = len(sortedPartynames[q])

# double loop, that compares, the sorted and unsorted,arrays and then where they are equal, the corresponding position of the old array, is used to call the corresponding position of the votes, array, which in effect is used to sort the votes array, based on the new sorted names array.... i know right.....
for l in range (len(sortedPartynames)):
    position = 0
    for b in range (len(Partynames)):
        if sortedPartynames[l] == Partynames[b]:
            difference = len(sortedPartynames[l]) - minimum
            #other formatting methods were not easy to get to work, so using the minimum counter, and a for, loop i am able to count the difference, of the length of the word, vs the minimum and take this into account so as to produce a formatted output, that spaces itself out, using the difference
            print(sortedPartynames[l]+ " "* (11 - difference) +"- " + (str(votescounter[b])))

    

    
  