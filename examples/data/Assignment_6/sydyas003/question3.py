#Print opening statements
print("Independent Electoral Commission\n--------------------------------")
print("Enter the names of parties (terminated by DONE):")

name=""#Initialise name to store inputs

user_input=[]#List to store

#While loop to add each input to a list, ends when 'DONE' is input
while (name!="DONE"):
    name=input()
    user_input.append(name) 
user_input.remove("DONE")

#Initialise list to store unique party names
parties=[]

#Populate parties with unique party names
for index in range (len(user_input)):
    if(user_input.index(user_input[index])==index):
        parties.append(user_input[index]) 
#Sort parties alphabetically
parties.sort()        
votes=[]

#Initialise all the elements of the votes list
for index in parties:
    votes.append(0)

#Calculate votes
for index_1 in range(len(parties)):
    for index in range(len(user_input)):
        if(user_input[index]==parties[index_1]):
            votes[index_1]+=1
            
print("\nVote counts:")
#Final output
for index in range(len(parties)):
    print("{0:<10} - {1}".format(parties[index],votes[index]))
    
