''' Counting number ofcharcter pairs 
Siphesihle Zwane 
09/05/14'''
def strng_pair(word):
    if len(word)<2:
        return 0
    elif word[0] == word[1]:
        return 1 + strng_pair(word[2:])
    else:
        return strng_pair(word[1:])
message=input("Enter a message:\n")
print("Number of pairs:",strng_pair(message))