"""Program count the number of votes for each political party in an election
Gary Finkelstein
22 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#create an array to store party names and a dictionary to store votes
parties = []
dict = {}
#allow user to input party names

user_input = input("Enter the names of parties (terminated by DONE): \n")
while user_input!= "DONE":
    parties.append(user_input)
    user_input = input("")  
    
#sort parties in order    
parties.sort()
#determining whether or not the dictionary contains a party name, and if it does, to add a vote to the corresponding party(key in dictionary)
for i in parties:
    
    if not i in dict:
        dict[i] = 0
    dict[i] = dict[i] + 1

print()
print("Vote counts:")
#creat new array to store alphebtically sorted array of parties
new = []

#put the party values in a new array
for i in dict:
    new.append(i)

#sort the new array
new.sort()
#print the party names and votes in columns of max width 10
for i in new:
    print(str(i) + " "*(10-len(i)) + " - " + str(dict[i]))
    