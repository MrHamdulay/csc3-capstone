#question2.py
#program checks if the number of pairs of adjacent letter
#romelon chetty
#07 may 2014
 
def pairs(word):
    #checks if the number of pairs of adjacent letter
    if len(word)<=1:
        return 0 #only one character-string cannot have a pair
    elif word[0]==word[1]: # checks if first equal second
        return 1 + pairs(word[2:]) # if so it returns 1 and adds a smaller string into the fuction from the third letter
    else:
        return 0 + pairs(word[1:])# otherwise it returns 0 and adds a smaller string into the fuction from the second letter

def main():
    string=input('Enter a message:\n') # gets input from user
    print ('Number of pairs:' ,pairs(string)) #returns number of pairs in string

main()