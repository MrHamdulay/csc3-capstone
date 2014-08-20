#Program that uses a recursive function to count the number of pairs of repeated characters in a string.
#Saul Bloch
#6 April 2014

user_string = input ("Enter a message:\n")

def pairs (user_sentence):
    if len(user_sentence) == 0 or len(user_sentence) == 1:
        return 0
    elif user_sentence[0] == user_sentence[1]:
        return 1 + pairs(user_sentence [2:])
    else:
        return 0 + pairs(user_sentence[1:])

print ("Number of pairs:",pairs(user_string))
 