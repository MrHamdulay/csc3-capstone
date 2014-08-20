#Amitha Doodnath - DDNAMI001
#08/05/2014
#Programme to count the number of repeated pairs of characters in a string


count=0

def countPair(word):
    global count

    if word=='':
        return count

    else:
        if(len(word)>1 and word[0]==word[1]):
            count=count+1
            return countPair(word[2:len(word)])
        else:
            return countPair(word[1:len(word)])




msg=input("Enter a message:\n")         

print("Number of pairs:",countPair(msg))