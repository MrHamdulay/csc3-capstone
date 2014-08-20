'''Program that uses a recursive function to count the number of pairs of repeated characters in a string.
Daniel M. Tamale
TMLDAN001
2014-05-08'''

word=input('Enter a message:\n')
def count(word):
    if word=='' or len(word)==1:
        return 0
    elif word[0]==word[1]:
        return 1 + count(word[2:])
    else:
        return count(word[1:])
print ('Number of pairs:',count(word))