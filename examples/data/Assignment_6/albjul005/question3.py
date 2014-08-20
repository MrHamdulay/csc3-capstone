"""Program for lists2
Julian Albert
ALBJUL005
2014-04-21"""

#function to get names of votes from user and convert into a list
def get_list():
    list_1 = [] #defines list_1
    string = '' #defines string
    print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
    string = input()
    while not string == "DONE":
        list_1.append(string)
        string = input()
    return list_1

#function that counts the number of votes for each party
def vote_count():
    list_1 = get_list()
    list_1.sort() #sorts the list
    check = []
    print("Vote counts:")
    for i in list_1:
        if i not in check:
            votes = list_1.count(i)
            check.append(i)
            format_for_votes = "{:<11}{}{}".format(i,"- ",votes)
            print(format_for_votes)
        
vote_count()
