# a program that uses a recursive function to count the number of pairs of repeated characters in a string
# mashau zwivhuya
# 5 may 2014
# get input
words=input("Enter a message:\n")
# printing words
print("Number of pairs: ",end="")
def words_pair(words,c):
    #counting words
    count=c
    if len(words)==1 or len(words)==0:
        return count

    else:
        if words[0]==words[1]:
            count+=1
            return words_pair(words[2:],count)
        # do recursion
        else:
            return words_pair(words[1:],count)
    

print(words_pair(words,0))
    
    
    