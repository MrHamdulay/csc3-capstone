def countPair(word):
    if (len(word) == 0):
        return 0
    else:
        firstChar = word[0:1]   #extract first letter of the string

        if (firstChar == word[1:2]): 
            return 1 + countPair(word[2:])#recursive step, word will be smaller because pairs are erased
        else:
            return countPair(word[1:])
        
n = input("Enter a message:\n")
print("Number of pairs:",countPair(n),end='')

