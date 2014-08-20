#Shaylan Lalloo
#LLLSHA008
#count pairs of equal letters


myin = input('Enter a message:\n')
#read input

def paircount(x):
    if len(x) <= 1:
        #if there is 1 or 0 letters, then there are no pairs
        return 0
    else:
        if x[0] == x[1]:
            #if there is a pair, increase the count and then start 2 letters later
            return 1 + paircount(x[2:])
        else:
            #if the letter is not in a pair, throw it out and continue
            return paircount(x[1:])

print('Number of pairs:', paircount(myin))
#output the answer
