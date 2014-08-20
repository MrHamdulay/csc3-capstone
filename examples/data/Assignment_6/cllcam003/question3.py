#Program that counts and displays number votes for party
#Cameron Collum
#24 April 2014
print("Independent Electoral Commission")
print("--------------------------------") # prints introduction
lis=[ ] # empty list
party=input("Enter the names of parties (terminated by DONE):\n") # allows user to input party names
lis.append(party) #adds party names to list
while party !="DONE": # allows user to add more party names until DONE is entered
    party=input("")
    lis.append(party)
del lis[len(lis)-1] # removes the word DONE from the list
lis.sort() #arranges words in list in alphabetic order
lis2=[] # creates new list for individual words
for i in lis: # checks if the word is in the list
    if i in lis2: # if it is, it moves onto the next word
        continue 
    else: # if not it adds the word to the list
        lis2.append(i)
repeat=[] 
for i in lis2:  # iterates through individual party names
    amnt=lis.count(i) # counts number of repetitions of word in list 2
    repeat.append(amnt) # adds the amount of votes for each word to list
print()    
print("Vote counts:")
for i in range(len(lis2)):
    print((lis2[i].ljust(11, " "))+"-",str(repeat[i])) # adjusts the words to have maximum width of 10 and prints words with amount of votes.


    
    
    