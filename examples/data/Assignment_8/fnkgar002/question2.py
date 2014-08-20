"""Program to count the number of pairs of repeated characters in a string
Gary Finkelstein
6 May 2014"""


def find_pairs (word):
    
    if len(word) == 1 or len(word) == 0:  #if the word length is 1 or 0, then the word will have no pairs
        return 0
    if word[0] == word[1]:                #if the word is found to have a pairing letter, then recall the function to repeat the process
        return 1 + find_pairs(word[2:])
    else:
        return 0 + find_pairs(word[1:])   #if the word is not found to have a pairing letter, then recall the function to repeat the process
    
#allows user to enter message 
user_input = input ("Enter a message:\n")
#displays number of pairs after calling the find pairs method
print ("Number of pairs: ", end="")
print(find_pairs(user_input))