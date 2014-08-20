""" programm to count the pairs of character recursively
Alexander Whiting
8 april 2014"""



def countpairs(sent):# counts the pairs of characters
    count = 0
    if len(sent)>=2:
        if sent[0] == sent[1]:
            count += 1
            return count + countpairs(sent[2:])
    else:
        return 0
    return count + countpairs(sent[1:])
        



sent = input("Enter a message:\n")
print("Number of pairs: "+str(countpairs(sent)))

