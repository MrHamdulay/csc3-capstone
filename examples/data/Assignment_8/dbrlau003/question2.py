#Lauren de Bruyn
#Counting number of pairs in a string
#9 May 2014

#get message from the user
message = input("Enter a message: \n")

#set pairs to 0
pairs= 0

def count_pairs(word):
    global pairs
    if len(word) <= 1:
        print("Number of pairs:", pairs)
    elif word[0] == word[1]:
        pairs= pairs + 1
        word = word[2:]
        return count_pairs(word)
    else:
        word = word[1:]
        return count_pairs(word)

count_pairs(message)
    