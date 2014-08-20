#Assignment 6 Question 3
#21 April 2014
#Alexi Kalamoudacos, Political Vote Counts


def VoteCount():
    x={}
    print('Independent Electoral Commission\n--------------------------------')
    y=input('Enter the names of parties (terminated by DONE):\n')
    while y!='DONE':
        if y in x.keys(): #Check to see if the vote has already been used before
            x[y]+=1 #If it has been voted for before, add 1 to the value of that key
        else:
            x[y]=1 #Else, create the new key
        y=input('')
    print()
    print('Vote counts:')
    for key in sorted(list(x.keys())): #Sort the dictionary into alphabetical order of keys
        print(key.ljust(10),'-',x[key])
if __name__=='__main__':
    VoteCount()