"""counting  the number of pairs of repeated characters in a string
Yondela Nkwali
06 May 2014"""

#ask for an in put
#use recursion function to find if any two letters in a row match
#printout the results

def counter (word):
    if len(word) == 0 or len(word) == 1:
        return 0
    elif word[0] == word[1]:
        return 1 + counter (word[2:])
    else:
        return 0 + counter(word[1:])
message=input("Enter a message:\n")
no=counter(message)
print("Number of pairs:",no)
