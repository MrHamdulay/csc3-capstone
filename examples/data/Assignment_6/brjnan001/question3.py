"""Assignment 6 Q3 Voting
Nandani Birjanund
23/04/14"""

print("Independent Electoral Commission") #prints the heading 
print("--------------------------------") #prints the second part of heading 

fruity = [] #creates an array to list fruit
counters = {} #counters in dictionary

fruit = input("Enter the names of parties (terminated by DONE): \n") #input from user, votes

while fruit != "DONE": #loop ends if fruit='DONE'
    fruity.append(fruit) #adds on to array list
    fruit = input() #allows for more input from the user 


for word in (fruity): #loop, to create dictionary
    if not word in counters:
        counters[word] = 0
    counters[word]+=1 #Used to count the occurence per letter

print()   
print("Vote counts:") #Vote counts printed 
y = "{0:<10}" #To format the data 

for word in sorted(counters): #solution for output
    print(y.format(word),"-",counters[word]) #function used to format enters "-"
