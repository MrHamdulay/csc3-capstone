"""Program to count number of votes
Khanyisile Morudu
20 April 2014"""

# At the end of the program, print out the names of the parties and their vote counts, with the parties listed in sorted order (the default order of the sorted function). Format party names in a field with width=10 to create the effect of columns - assume all party names are at most 10 characters wide.

print("Independent Electoral Commission")
print("--------------------------------")

#creating initial data
names = []
votes = []
counter= []
votes_sort = []
counter_sort = []
string= input("Enter the names of parties (terminated by DONE):\n")

#creating names  list
while string.upper() != "DONE":
    names.append(string)
    string = input("")

#voting list
for i in range(len(names)):
    if i == len(names):
        break        
    votes.insert(i,names[i])
    num = names.count(names[i])
    counter.insert(i,num)
    while votes[i] in names:
        names.remove(votes[i])
    names.insert(i, votes[i])
  
#sorting the list

#creating a list of lists
all_voting = zip(votes, counter)

#sorting it out
all_sorted = sorted(all_voting)

#"unlisting" the list (learnt online)
new_votes = [point[0] for point in all_sorted]
new_counter = [point[1] for point in all_sorted]


#printing in formatted manner
print("\nVote counts:")
a = "{0:<10}"
for i in range(len(new_votes)):
    print(a.format(new_votes[i]), "-", new_counter[i])
        

