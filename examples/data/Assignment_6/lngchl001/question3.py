#program to count the number of votes for each political party
#By Chloe Longmore
#23 April 2014

#fix second occurences of orange??
#fix placing of dash in output

#greeting
def intro():
    print("Independent Electoral Commission")
    print("--------------------------------")

import collections
#function that ask the user for input of party names and counts them
def votes():
    print("Enter the names of parties (terminated by DONE):")
    list_parties=[]
    #appends entered items into a list
    while True:
        list1=input("")
        if list1=='DONE':
            break
        list_parties.append(list1)
    #converts list into dictionary with corresponding counted values
    counted=dict((i,list_parties.count(i)) for i in list_parties)
    #alphabetically sorts the dictionary keys and corresponding values
    ordered=collections.OrderedDict(sorted(counted.items()))
    print()
    print("Vote counts:")
    #prints votes and their counts
    for i in ordered:
        length_spacing=(10)
        print("{0:<{2}} - {1}".format(i,counted[i],length_spacing))

intro()
votes()