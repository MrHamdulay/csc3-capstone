# Emmalene Naicker
# NCKEMM001
# Question 3

v = []

print("Independent Electoral Commission\n--------------------------------")

# Ask user to enter the names of the parties
p = input("Enter the names of parties (terminated by DONE):\n").lower()

# Get list
while p != "done":
    exists = False
    for i in range (len(v)): 
        if p in v[i]: # This will check to see if the party exists
            v[i][1] += 1 # Add one to the number of votes
            exists = True 
            
    if not exists:  
        v.append([p, 1])
    p = input().lower()

   
print("\nVote counts:")
v.sort() # Used to sort list

for i in range (len(v)):
    r = "{0:<10}".format(v[i][0]) 
    print(r, "-",v[i][1])
        
    
    
    
