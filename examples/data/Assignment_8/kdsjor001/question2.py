"""Assignment 8 Question 2
06 May 2014
Jordan Kadish, Checking for Paired Letters"""

def PairChecker(word):
    if len(word)==2:
        if word[0]==word[1]:
            return 1
        else:
            return 0
    elif len(word)<2:
        return 0
    elif word[0]==word[1]:
            return 1+PairChecker(word[2:])
    else:
        return PairChecker(word[1:])
CheckWord=input('Enter a message:\n')
print('Number of pairs:',PairChecker(CheckWord))