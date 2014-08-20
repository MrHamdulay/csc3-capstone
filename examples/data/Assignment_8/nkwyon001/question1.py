"""checking if a word is a palindrome
yondela nkwali
06 May 2014"""

#finding the reversed string
def reverse(word):
            if word == "":
                        return word
            else:
                        return word[-1] + reverse(word[:-1])  
#asking for an input
word=input("Enter a string:\n")
string=reverse(word)
#comparing input to reversed word and printout results
if string == word:
            print("Palindrome!")
else:
            print("Not a palindrome!")
