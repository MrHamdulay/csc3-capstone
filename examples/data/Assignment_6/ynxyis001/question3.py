#Vote counter
#Jennifer Yuan
#23 April 2014

print("Independent Electoral Commission") #prints heading
print("-"*32)

party = {} #empty dictionary
names = input("Enter the names of parties (terminated by DONE):\n") #gets input from user
while names != "DONE": #DONE = sentinel
   if names not in party: #if name inserted is not already in list (key), then create a new entry (key) in party with value = 1
      party[names]=1
   else:
      party[names]+=1 #if name is already in list (key), then just adds a value to already existing value 
   names = input ("") #continues loop
   
print("\nVote counts:") #heading

for i in sorted(party): #sorting dictionary
   y = party[i] #gets value of key
   z = "{0:<10}".format(i) #creates a field of width 10  
   print(z, "-", y)   #prints name of party and its respective votes
   
   
   