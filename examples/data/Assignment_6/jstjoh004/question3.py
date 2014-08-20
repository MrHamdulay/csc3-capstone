# program to count the number of votes for each political party
# hendrik joosten
# 24/04/2014

#declare the variable votes in
vote = []

# print the header
print("Independent Electoral Commission")
print("--------------------------------")

# populate vote
name = input("Enter the names of parties (terminated by DONE):\n")
while name != "DONE":
      vote.append(name)
      name = input ("")

# make a new array with unique party names
parties = []
for i in range(len(vote)):
      if parties.count(vote[i]) == 0:
            parties.append(vote[i])
            
            
# sort unique party names            
parties = sorted(parties)

# count the votes per party
x = 0
partyvotes = []
for j in range(len(parties)):
      x = vote.count(parties[j])
      partyvotes.append([parties[j],x])

# print header
print("")
print("Vote counts:") 

# print the formatted list
for k in range(len(partyvotes)):
            print(partyvotes[k][0] + " "*(10-len(partyvotes[k][0])),end="")
            print(" -",partyvotes[k][1])
      
      


      

      

