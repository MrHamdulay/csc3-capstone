# Assignment 6
# Program to take in votes and tally them
# Frans van Hoek   
# 22 April 2014

def get_votes():
    votes = {}
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    while True:
        party = input("")
        if party == 'DONE':
            break
        elif party in votes:
            votes[party] += 1
        else:
            votes[party] = 1
    return votes


def print_votes(dic1):
    
    print()
    print("Vote counts:")
    list1 = []
    for i in dic1:
        list1.append(i)
    list1.sort()
    for i in list1:
        space = 10 - len(i)
        print(i + space*' '+ ' -', dic1[i])
    
x = get_votes()
y = print_votes(x)

