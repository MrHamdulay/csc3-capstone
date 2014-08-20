#Assignment 6: Question 3
#By: Litha Maqungo
# 24 April 2014
def votecount():
    print("Independent Electoral Commission")
    print("--------------------------------")
    vote=input("Enter the names of parties (terminated by DONE):\n")
    print()
    first_list=[] # checks for the first time it occurs
    second_list=[] #makes sure there's no duplication
    while vote!="DONE": #sentinal
        if vote not in first_list: #if beyond first
            first_list.append(vote) #add word to the list
        else:
            second_list.append(vote) 
        vote=input() #allows for the input again
    first_list.sort() #sorts out what's in the list
    print("Vote counts:")
    for i in first_list: #first occurences
        count= second_list.count(i) #counting how many times it's in the respective listd
        print("{:<10}".format(i)+" -",count+1) # printing with format 

votecount()
    
