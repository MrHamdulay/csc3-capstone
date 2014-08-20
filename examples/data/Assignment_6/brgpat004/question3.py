'''Q3 of Assignment 6: Program to count votes for each political party in an election
Patrick Boroughs
21 April 2014'''

print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")

#Input first value, create empty list
string=input()
list=[]

while string!="DONE": #end when user types 'DONE'
    list.append(string) #add value to list
    string=input() #input new value

#Sort list    
list.sort()

#Create temporary string to test if same item has already been printed
temp='null'
print("\nVote counts:")

#loop through list
for string in list:
    
    if string!=temp: #Test if string has been printed
        
        temp=string #assign new string to temp variable
        print(string,((9-len(string))*' '),'-',list.count(string)) #print