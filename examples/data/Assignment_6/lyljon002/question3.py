#20 April 2014  
#Assignment 6, Question 3, count votes for each party in an election
#LYLJON002

dicVotes = {}                                   #declare dictionary
string = ''


print("Independent Electoral Commission")        #heading print
print("--------------------------------")
string = input("Enter the names of parties (terminated by DONE):\n")    #get first string



while string != "DONE": 
        if string in dicVotes.keys():
                dicVotes[string] = dicVotes[string] + 1         #add votes to a votee name
        else:
                dicVotes.update({string : 1})                 #create votee name, score of 1
        string = input("")
        

print("\nVote counts:")         #heading of list

dicVotes2 = sorted(dicVotes.keys())             #sort the dic alphabetically

for j in dicVotes2:
        print(j + " "*(11-len(j)) + "- " + str(dicVotes[j]))    #output votes
        
