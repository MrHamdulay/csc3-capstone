"""Sphiwe Muthembi
MTHSPH007
qUESTION 3 ASSIGNMENT 6"""


def elections():
    """counts number of votes"""

    print("Independent Electoral Commission")
    print("--------------------------------")
    make_vote = input("Enter the names of parties (terminated by DONE):\n")
    input_values = {}
    
    
    if make_vote == "DONE":
        print("\nVote counts:")

    else:

        input_values[make_vote] = 1 

        while True:
                make_vote = input()
                if make_vote == "DONE": 
                    break
                if make_vote not in input_values: 
                    input_values[make_vote] = 1 
                else:
                    input_values[make_vote] += 1 

        mylist = list(input_values.keys()) #returns a list of candidates for sorting
        print("\nVote counts:")

        for party in sorted(mylist): 
       
            print("{0:<10} - {1}".format(party, input_values[party]))

elections()