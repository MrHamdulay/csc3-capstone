# This program prompts the user to enter a list of strings and these strings are 
# then printed in the same order but without duplicates.
# Uses the sentinel "DONE" to end the input list.

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 29 April 2014

askuser = input("Enter strings (end with DONE):\n")
thelist = [] # stores the original unsorted list
listunique = [] # stores the unique list with no duplicates
thedict = {} # unsorted unique list items

while askuser != "DONE":
    thelist.append(askuser)
    askuser = input()

# Populate the dictionary and sorted unique list
for i in thelist:
    if not i in thedict:
        thedict[i] = 0
        listunique.append(i)
    thedict[i] += 1

# print the unique list
print("\nUnique list:")
for j in listunique:
    if j in thedict:
        print(j)

#Sample I/O:

#Enter strings (end with DONE):
#the
#old
#man
#and
#the
#sea
#DONE

#Unique list:
#the
#old
#man
#and
#sea