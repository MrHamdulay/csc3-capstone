# A program that counts the number of pairs in an input message using recursion
# Martin Batek
# 5 May 2014

def countpairs(word):
    """A program that counts the number of pairs in the parameter using recursion"""
    if len(word) == 2:
        if word[0] == word[1]:
            return 1
        else:
            return 0
    elif len(word) < 2:
        return 0
    else:
        if word[0] == word[1]:
            return 1 + countpairs(word[2:])
        else:
            return 0 + countpairs(word[1:])
        
message = input("Enter a message:\n")
pairs = str(countpairs(message))
print("Number of pairs:",pairs)