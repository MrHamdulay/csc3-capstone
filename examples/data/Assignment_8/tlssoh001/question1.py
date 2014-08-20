'''Sohail Tulsi
TLSSOH001
a check to see if a word is a palindrone'''

word=input("Enter a string:\n")  #user input string

#to check the word is the same reversed
def check(word):       
    if word == '':         
        return True

    else:
        if (ord(word[0]) == ord(word[len(word)-1])):
            return check(word[1:len(word)-1])

        else:
            return False

if(check(word)==True):
    print("Palindrome!")

else:
    print("Not a palindrome!") 
