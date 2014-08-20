#2014/04/23
#Election parties
#Kelly Goosen

print("Independent Electoral Commission") 
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
names=[] #initiating empty list
name1="" #initiating empty string
name1 = input() #getting inputs from user
max_length = 0 #not necessary
while name1 != 'DONE':
       if len(name1)>max_length:
              max_length=len(name1) #not necessary
       names.append(name1) #add name1 to list
       name1 = input() #get more inputs from user
print()
    
list=[] #initiating new empty list
for i in range(len(names)): #itterate through length of list
       if not names[i] in list:
              list.append(names[i]) #add to list
              list.sort() #sort list into alphabetical order

print("Vote counts:")
for i in list:
       votes = names.count(i) #count votes
       print(i.ljust(10), '-' , votes) #print party then nr of votes alongside