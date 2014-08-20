"""Assignment 6, Question 3
JT
23-04-2014"""

#function to get names of votes from user and convert into a list
def get_list():
    list1 = []
    word = ''
    print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
    word = input()
    while word != "DONE":
        list1.append(word)
        word = input()
    return list1

#function that counts the number of votes for each party
def vote_counts():
    list1 = get_list()
    list1.sort()
    check = []
    print("\nVote counts:")
    for i in list1:
        if i not in check:
            votes = list1.count(i)
            check.append(i)
            frmt = "{:<11}{}{}".format(i,"- ",votes)
            print(frmt)
        

vote_counts()
