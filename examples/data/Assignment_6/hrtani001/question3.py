#Count Votes
#Aniq Hartle
#25/04/2014

print(
"Independent Electoral Commission\n\
--------------------------------\n\
Enter the names of parties (terminated by DONE):")

#initialise variables
str_list = []
i = str
D = {}

#take input and add to list
while i != "DONE":
    i = input()
    str_list.append(i)
#cut the last entry out (DONE)    
str_list = str_list[:len(str_list)-1]

#If the entry does not exist in the dictionary, add it otherwise add a vote
for i in range(len(str_list)):
    if str_list[i] not in D:
        D[str_list[i]]=1
    else:
        D[str_list[i]]+=1

#print output
print("\nVote counts:")
for i in sorted(D.keys()):
    print("{:<10} - {}".format(i,D[i]))