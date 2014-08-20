"""Program to count votes for a political parties
JP Lanser
19 April 2014"""

opening_line = "Independent Electoral Commission"
dash = len(opening_line)

print(opening_line)
print('-' * dash)

# Prompt user for their vote and use 'WHILE loop' to keep prompting until DONE is entered
# Make a dictionary to keep track of the different parties and the number of votes per party


vote = input("Enter the names of parties (terminated by DONE): \n")

vote_collection = {} #Empty dictionary created

while not vote =="DONE":    
            if vote not in vote_collection:
                        vote_collection[vote] = 1 #If this party hasn't been voted for yet, it is now in the dictionary with 1 vote
            else: vote_collection[vote] +=1       #This party now has an additional vote 
            vote = input()                        # Keeps prompting user until DONE is entered

# Now create a list to store the party names so that they can be printed in alphabetical order (using sort function)
#Create this new list by looping through the dictionary and appending the party names

names =[]
for i in vote_collection:
            names.append(i)
            
            
names.sort()

  
print()
print("Vote counts:") #Required format as per Sample I/O

            #Loop through the list, print each party name, print the number of votes per party, they are stored in the dictionary(vote_collection)
for i in names:
            formatted="{0:<10}".format(i)   #Format as required, assume party names are a max of 10 characters wide
            print(formatted, "-" , vote_collection[i] ) #vote_collection[1] is the number of votes (stored in dictionary)
            
            
           
           
           
            



            






