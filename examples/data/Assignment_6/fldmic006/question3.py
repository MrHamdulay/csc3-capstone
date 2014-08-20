#program to enter political parties and calc the number of votes each recieves
#michael field
#21 april 2014

#increases counter for every unique value in list
def count (lis, value):
    
    counter = 0
    for item in lis:
        if item == value:
            counter += 1
    return counter


#print heading
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
parties = []
input1 = ""

#input parties into the array
while (input1 != "DONE"):
    input1 = input("")
    parties.append(input1)

#remove DONE from the list of names
parties.remove("DONE")

vote = 0
print("\nVote counts:")

#count the votes
#create dictionary
counter = {}

for party in sorted(parties):
    if not party in counter:
        counter[party] = 0
    counter[party] += 1
    
for i in sorted(counter):
    print(i, " "*(10-len(i))," - ", counter[i], sep = "")