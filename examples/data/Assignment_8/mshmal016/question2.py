'''function to count number of pairs
matshepo mashabela
06 may 2014'''

def countpairs(sentence):
    if len(sentence)<2:
        return 0
    elif sentence[0]==sentence[1]:
        return 1+countpairs(sentence[2:])

    else:
        return countpairs(sentence[1:])

sentence=input("Enter a message:\n")
print("Number of pairs:",countpairs(sentence))
    
