
def countpairs(sentence):
    if len(sentence)==1:
            return 0
    elif len(sentence)==2:
        if sentence[0]==sentence[1]:
            return 1  
        else:
            return 0
    elif sentence[0]==sentence[1]:
        sentence=sentence[2:]
        return (1+countpairs(sentence))
    else:
        sentence=sentence[1:]
        return countpairs(sentence)
                
sentence=input("Enter a message:\n")
print("Number of pairs:", countpairs(sentence))