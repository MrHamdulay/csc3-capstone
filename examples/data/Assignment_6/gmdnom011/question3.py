# Program to count votes
# Nomsa Gamedze
# 21 April 2014

def main():
    print("Independent Electoral Commission", "--------------------------------", "Enter the names of parties (terminated by DONE):", sep='\n')
    votes = []
    vote = input("")
    while vote != "DONE":
        votes.append(vote)
        vote = input("") 
    votes = sorted(votes)
    print('\n'"Vote counts:")
    y = set(votes) # removes duplicate strings
    y = sorted(y)
    for i in y:
        count = votes.count(i)
        print(i.ljust(10), "-", count)

main()
    