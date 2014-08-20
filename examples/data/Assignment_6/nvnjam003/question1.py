#James Nevin
#Assignment 6, Question 1
#23/04/2014

print ("Enter strings (end with DONE):")
entries = [] #Empty list for entries
userString = "" #Empty string for user's word
maxLength = 0 #Variable for longest string
while (userString != "DONE"):
    userString = input()
    if (len(userString) > maxLength and userString != "DONE"): #If longer than longest string
        maxLength = len(userString)
    entries.append(userString) #Adding to list
entries.remove("DONE") #Removing final entry
print ("\nRight-aligned list:")
for item in entries:
    print ((maxLength-len(item))*" " + item) #Printing spaces then item