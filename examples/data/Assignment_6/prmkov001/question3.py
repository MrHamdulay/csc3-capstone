#Kovlin Perumal
#21/04/14
#Question3 - Voting System

print("Independent Electoral Commission")
print("--------------------------------")#Output Header 


names = []
votes = []

name = input("Enter the names of parties (terminated by DONE):\n")
count = 0

while name != 'DONE' :#Initialise while loop with DONE as exit
      
      
      if(name in names) :
            votes[names.index(name)] += 1 #Check if name already entered
            
      else :
            names.append(name)
            votes.append(1) #else add name
            
      count += 1       
      name = input("")


dictvotes = {}

for i in range(len(names)) :
     dictvotes[names[i]]=votes[i] #Insert arrays  into a dictionary                                                             
      
names.sort() #sort names

print()
print("Vote counts:")
                  
for i in names:
      print(i + (" " * (10 - len(i))), "-", dictvotes[i]) #Display vote corresponding to name

