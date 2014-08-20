"""Assignment 6 question 3
shannon clacey
23 april 2014"""
def vote():
    x ="Independent Electoral Commission" #print the format given
    len_x = len(x)
    print(x)
    print("-"*len_x, sep='') #printing the dashes of the format
    vote = input("Enter the names of parties (terminated by DONE):\n") #get the name of the party
    print()
    list2 = [] #this list is put in place to check for any duplicates
    list1 = [] #this list checks to find the first occurence of the word within the list
    while vote != "DONE":
        if vote not in list1: #if the given party as not yet been mentioned
            list1.append(vote)
        else: #if the given party has already been mentioned
            list2.append(vote)
        vote = input() #continually getting input from user without reprinting input statement
    list1.sort() #the sort function puts all the items in alphabetical order for printing
    print("Vote counts:")
    for i in list1: #this iterates throught the first list with all the first occurences of the word
        count = list2.count(i) #this counts the number of time that the words in the first list come up in the second list
        print("{:<10}".format(i)+" -",count+1) #this is the final print statement. It is necessary to add one onto the count statement because i have essentially subtracted one from the total by putting the first occurence in a separate list
vote()        
    