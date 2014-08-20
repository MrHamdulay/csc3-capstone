"""Program to count the number of pairs of strings in a sentance recursivly
Dean Gracey
4 May 2014"""


def countpairs(word):
    count = 0
    
    if(len(word)<2):
        return count
    if(word[0]==word[1]):
        count+=1
        word = word[2:len(word)]
    else:
        word = word[1:len(word)]
    return count + countpairs(word)

word = input("Enter a message:\n")
print("Number of pairs: ", end = "")
print(countpairs(word))
