""" Q1 of Assignment 7: List without duplicates
Shaheel Kooverjee
1st May 2014 """

print("Enter strings (end with DONE): ")

duplist = [] #user unput list (possibly containing duplicates)
unlist = [] #unique list containing no duplicates

while True: 
    item = input("")
    if item == "DONE": #loop broken if DONE entered
        break
    else: duplist.append(item) #adds user's string to list
    
for i in duplist: 
    if i not in unlist:
        unlist.append(i) #add string to unique list if not already in unique list
        
print()
print("Unique list: ")
for j in unlist: #print each item of unique list
    print(j)