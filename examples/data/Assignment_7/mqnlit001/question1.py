#Assignment 7: Question 1
# By: Litha Maqungo
# printing list without duplicates 

instruction= input(("Enter strings (end with DONE): \n")) #prompting input from the user
string_list=[] #empty string created for the list
duplicate_list=[] #empty string that is the duplicate list which is irrelevant
while instruction != "DONE": #Looping until it receives the input DONE
    if instruction not in string_list:
        string_list.append(instruction) #adding the new string to the first list
    else:
        duplicate_list.append(instruction)#adding the new string to the duplicate list
    instruction=input() #allows for the next input
print() #making sure there's space printed between the two lists
print("Unique list:") #printing out Unique list
for i in string_list: #looping to make sure it prints out the data in the list
    print(i)
    
        
        
