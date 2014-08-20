#Chantel Foot
#Question 1, assignment 6


names=[] #start off with empty string
list_names = input("Enter strings (end with DONE):\n") #get list of names from user
while list_names != "DONE": 
    names.append(list_names) #add all names to empty list
    list_names = input("")

maximum=0 #begin maximum length of words at 0
for i in range(0,len(names)): 
    #print (names[i]) #printing the name at a specific index value
    if len(names[i])>maximum: #if the length of word printed is has a greater maximum, change maximum. 
        maximum=len(names[i]) #repeats until finds the maximum word in the list
        
print()
print("Right-aligned list:") #heading before prints the list right-aligned

for i in range(0,len(names)):
    print((maximum-len(names[i]))*" ", names[i],sep="") #get maximum number of spaces, print spaces
    

