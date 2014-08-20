#Assignment 6
#Question 3
#Rabia Parker
#Due Date:25/04/14

#print statements

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

#initialise variables
choice = ""
listparties = [] #create list
while choice != "DONE": #enter choice
    choice = input()
    if len(choice) <= 10 and choice != "DONE": 
        listparties.append(choice) #populate list with elements

outcome = []
for i in range(len(listparties)):
    if not listparties[i] in outcome:
        outcome.append(listparties[i])
        
outcome.sort()

numbers=[]
for i in range(len(outcome)):
    sum = 0
    for j in range(len(listparties)):
        if outcome[i] == listparties[j]:
            sum+= 1
    numbers.append(sum)
    
#print outcome
print()
print("Vote counts:")      
for i in range(len(outcome)):
    print(outcome[i] , (10 - len(outcome[i]))*" " , " - " , numbers[i],sep="")