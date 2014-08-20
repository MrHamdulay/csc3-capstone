#Code to count the number of votes for each political party in an election
#Saul Bloch
#22 April 2014


print("Independent Electoral Commission")
print("--------------------------------")
#creating dictionery and array
Array = []
new_Array = []
dict = {}
#adding inputs to array until 'DONE' is inputted
names = input("Enter the names of parties (terminated by DONE):\n")
while names != "DONE":
    Array.append(names)
    names = input()
#transferring information from array into dictionery
for i in Array:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1
    
#transferring information back into Array and sorting Array
for i in dict:
    new_Array.append(i)
new_Array.sort()

#printing votes
print()
print("Vote counts:")

for i in new_Array:
    print(str(i)+" "*(10-len(i))+" - "+str(dict[i]))
