#glnrus002
#question 3
#Write a program to count the number of votes for each political party in an election. Your program must accept a sequence of names of parties (terminated by the word DONE) and keep track of the votes per party. There is no pre-determined party list so the list must be created as party names are encountered.
import collections

def vote():#bALLOTS CAST
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):\n")
    parties=[]
    i=0
    tmp=""
    while tmp !="DONE":
        tmp=input()
        parties.append(tmp)
        i+=1
    del parties[len(parties)-1]
    return parties 

def count(parties):#used to count votes
    number_of_votes=len(parties)
    votes=[]
    tmp=""#used to compare whether input is unique
    for i in range(number_of_votes):
        votes.append(parties.count(parties[i]))
    return votes

def output(parties,votes):#displays output
    form=form="{0:<10}"
    #finally print
    print("Vote counts:")
    #=======alphabetic=======
    display=[]
    for i in range(len(parties)):
        display.append(form.format(parties[i])+" - "+str(votes[i]))#appends name of party to amount of votes then stores them as a single string that can be ordered to alphabetical order later
    display.sort()

########################rEMOVE DUPLICATES######################################################
    count=1
    for j in range (len(display)):
        for i in display:
            if j<=len(display)and j>0:
                if display[j-1]==i:
                    del display[j-1]  
        count+=1
        
    for i in range (len(display)-1):
        if display[i]==display[i+1]:
            del display[i]
       
#####################PRINT OUT##################################################################    
    count=0#reset counter
    for i in display:   
        print(display[count])
        count+=1
               
if __name__=="__main__":
    parties=vote()
    votes=count(parties)
    output(parties,votes)
           
