# A program to count the number of votes for each party
# Created by: Jenna Lake
#Date: 25/4/2014

def get_string():
    list_party=[]
    a=True
    count=0
    print("Independent Electoral Commission")
    print("--------------------------------")
    c=input("Enter the names of parties (terminated by DONE):\n")
    while a:
        if c=='DONE':
            break
        else:
            list_party.append(c)        # append each new vote to the end of the string
        count+=1
        c=input()

#def search():
    newstring=[]
    unsortstring=[]
    for i in list_party:                
        if i not in newstring:          #counts number of each original party once
            y=list_party.count(i)
            newstring.append(i)         #make a list of each unique party (ie checks if a party has been counted already)
            t=str(i+" "*(10-len(i))+ " - "+str(y))
            unsortstring.append(t)

    
#def sort():
    print("\nVote counts:")
    for i in sorted(unsortstring):      #sorts the string alphabetically
            print (i) 

get_string()    
