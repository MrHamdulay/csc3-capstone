# Kate Bell
# BLLKAT005
# 22 April 2014 

print("Independent Electoral Commission\n--------------------------------")
party = input("Enter the names of parties (terminated by DONE):\n")

# Count the number of times each party is voted for in a dictionary
party_list = {}
while not party == "DONE":
    if not party in party_list:
            party_list[party] = 1
    else:
            party_list[party] += 1      
    party = input("")
    
# Convert the dictionary into a 2D array and sort it
party_array = []
for a in party_list:
    temp_list = [a,party_list[a]]
    party_array.append(temp_list)

party_array.sort()

# Print the number of votes per party
print("\nVote counts:")
for i in range(len(party_array)):
    print(party_array[i][0]," "*(11-len(party_array[i][0])),"- ",party_array[i][1],sep="")


