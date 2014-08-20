"""PRIYANKA GOBERDHAN
ELECTION VOTE
25/04/2014"""

print("Independent Electoral Commission")
print("--------------------------------")

x = input("Enter the names of parties (terminated by DONE):\n")

user_input = [ ]

while (x != "DONE"):
    user_input.append(x)    
    x = input()
parties = []
for party in range (len(user_input)):
    if (user_input.index(user_input[party])==party):
        parties.append(user_input[party]) 
parties.sort()        
count = []

for i in parties:
    count.append(0)

for i in range(len(parties)):
    for party in range(len(user_input)):
        if(user_input[party]==parties[i]):
            count[i] += 1
            
print("\nVote counts:")

for i in range(len(parties)):
    print("{0:<11}- {1}".format(parties[i],count[i]))

   
