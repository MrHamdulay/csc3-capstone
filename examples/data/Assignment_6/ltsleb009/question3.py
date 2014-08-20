#-------------------------------------------------------------------------------
# Name:        Question3
# Purpose:     Assignment 6
#
# Author:      Taylor
#
# Created:     24/04/2014
# Copyright:   (c) Taylor 2014
#-------------------------------------------------------------------------------
def main():
    """counts number of votes"""

    print("Independent Electoral Commission")
    print("--------------------------------")
    data = {} #creat an empty dictionary
    nominee = input("Enter the names of parties (terminated by DONE):\n")

    if nominee == "DONE":
        print("\nVote counts:")

    else:

        data[nominee] = 1 #assign nominee to value of 1 for 1 vote

        while True:

                nominee = input()

                if nominee == "DONE": #Sentinel
                    break
                if nominee not in data: #check to see if nominee in data, if not, append
                    data[nominee] = 1 #assign new nominee to 1 vote
                else:
                    data[nominee] += 1 #bump the vote by one if nominee already in data

        mylist = list(data.keys()) #return a list of nominees for sorting
        print("\nVote counts:")

        for party in sorted(mylist): #iterate over sorted list
        #print the party together along with the number of votes it has obtained
            print("{0:<10} - {1}".format(party, data[party]))

if __name__ == '__main__':

    main()
