'''Program counting the number of votes
Sbongakonke Mlangeni
22 April 2014'''

print('Independent Electoral Commission\n--------------------------------')
def xy():
    #Get votes
    parties = input('Enter the names of parties (terminated by DONE):\n')
    print('')
    parties_list = []
    
    #Termination conditiuon
    while parties != 'DONE':
        parties_list.append(parties)
        parties = input('')
    #Sorting
    #parties_list.sort()
    a = parties_list
    #print(a)
    
    #Creating a dictionary
    from collections import Counter
    Keys_Values = Counter(a)
    #print(Keys_Values)
    
    #Extracting the keys
    PartiesNames = Keys_Values.keys()
    #print(PartiesNames)
    
    #Extracting the valutes
    PartiesFrequencies = Keys_Values.values()
    #print(PartiesFrequencies)
    partiesnamesnewlist = []
    
    
    #Creating a list from the extracted values and sorting them
    for i in PartiesNames:
        partiesnamesnewlist.append(i)
    partiesnamesnewlist.sort()
    #print(partiesnamesnewlist)
    
    #Matching the values with the keys on seperate lists
    partiesfrequenciesnewlist = []
    for i in partiesnamesnewlist:
        a = Keys_Values[i]
        partiesfrequenciesnewlist.append(a)
    #print(partiesfrequenciesnewlist)
    
    
    #Pritning out the output
    print('Vote counts:')
    for i in range(len(partiesnamesnewlist)):
        this = '- '
        value = str(partiesfrequenciesnewlist[i])
        
        print('{0:<10}{1:>4}'.format(partiesnamesnewlist[i],this+value))
        
xy()