'''Phillip Ruhesi
24/04/14
this is a program to count the number of times a parties name is input'''
grid={}              #create empty dictionary

x=input('Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n')

while x!='DONE':            #Infinite loop until the user inputs done
    if x in grid:
        grid[x]+=1          #Adds the words entered to the dictionary and increases their value by 1 for each occurence
    else:
        grid[x]=1
    x=input()

parties=[]
k=grid.keys()               #gets a list of the keys in the dictionary
for i in k:
    parties.append(i)             #adds all the keys in the dictionary to the list parties
parties.sort()
print('\nVote counts:')
for j in parties:                            
    #print(j,'-',grid[j])
    print('{0:' '<11}- {1}'.format(j,grid[j]))    #adds a space of 11 after the name of the party then prints a hyphen and a space followed by the number of occurences

