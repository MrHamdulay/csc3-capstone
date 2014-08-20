#Program to count the number of votes for each political party
#Ethan Jackson  `
#23 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
names = ""
lis = []
while names != "DONE": #creates a sentinel loop where "DONE" is the terminator
    names = input("")
    lis.append(names) #adds each name to the list   
    continue
lis.remove("DONE")#removes "DONE" from the list
lis = sorted(lis)
counter = {}
for i in lis:#runs through list
    if not i in counter:
        counter[i] = 1#counter remains 1 if only one vote
    else:
        counter[i] += 1#adds one vote for every consecutive occurence of party
print("\nVote counts:")
for i in sorted(counter):#runs through alphabetical list
    print(i, (9 - len(i))*' ',"-", counter[i])

    
    
        