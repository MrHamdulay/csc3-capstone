"""Name: Sibulele Hlongwane
Date:    20 April 2014
Program Function: Count number of votes"""

print("Independent Electoral Commission")
print("--------------------------------")
#Creates Empty list
x=[]
y=[]
#Prompts user to enter list of names
names= input("Enter the names of parties (terminated by DONE): \n")
#Repeats prompt until the user enters the sentinel, being Done
while (names!="DONE"):
    #adds names into x list(x list will be manipulated)
    x.append(names)    
    #adds names into y list, as a copy of the x list(y is not changed)
    y.append(names)
    
    names=input()
#prints heading
print("\nVote counts:")

#counts the number of votes, and removes repeitition of the "category" from the x list, to prevent duplication of voting.
for a in y:
    for j in range((x.count(a))):
        if x.count(a)>1:
            x.remove(a)
            
#sorts x array into alphabetical order
x.sort()

#prints the votes, and determines a space count depending on the length of the word
for a in x:
    print(a," "*(9- len(a)),"-",y.count(a))
 
