# Vote counter
# Khwezi Majola
# MJLKHW001
# 20 April 2014

def count():
    print('Independent Electoral Commission\n--------------------------------')
    P = [[]]#Empty 2d list
    party = input('Enter the names of parties (terminated by DONE):\n')
    iCount = 0 #Party Counter
    if party != 'DONE':
        P[0].append(party)
        P[0].append(0)
        iCount += 1
        for i in range(len(P)): #Find the position of the party
            if (party in P[i]) == True:
                iTemp = i
                break
        P[iTemp][1] += 1 
        iCheck = 0
        party = input() #Asks for another input
    while party != 'DONE': #Continues to ask for parties
        J = []#Empty list for later use
        for i in range(len(P)):
            if party in P[i]: #Ensures there are no duplicate parties
                iCheck = 1
                break
        if iCheck == 0:
            P.append(J) #Add empty list to the list
            iPos = P.index(J)
            P[iPos].append(party)
            P[iPos].append(0)  
            iCount += 1
        for i in range(len(P)): #Find the position of the party
            if (party in P[i]) == True:
                iTemp = i
                break
        P[iTemp][1] += 1
        party = input() #Asks for another input
        iCheck = 0
    output = '' #Empty output string for later use
    print('\nVote counts:')
    P.sort()
    if iCount > 0:
        for i in range(len(P)): #Loops through the list
            output = '{0:<10} - {1}'.format(P[i][0], P[i][1])
            print(output)
count()