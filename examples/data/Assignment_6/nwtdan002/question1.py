"""Aligning a list of strings to the right
By Daniel Newton
19/04/14"""

print("Enter strings (end with DONE):") #Prompts user input

#Defines variable and list to be used
run=True
lenmax=0
stringlist=[]

while run:      #Indefinite loop that adds strings to the variable strinlist until the user types DONE
    string=input()
    
    if string=="DONE":
        break
    
    if len(string)>lenmax:  #Finds the length of the longest string of all inputs
        lenmax=len(string)
    stringlist.append(string)  #Adds input to list

   
print()
print("Right-aligned list:")

for i in stringlist:     #Splits up the compiled stringlist and prints each one aligned to the right, by printing blank spaces before the word equal to the length of the longest word minus the length of the word currently being evaluated.
    print(" "*(lenmax-len(i))+i)