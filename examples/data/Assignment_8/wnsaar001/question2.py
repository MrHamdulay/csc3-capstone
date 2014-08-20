"""pair finding program
Aaron Weinstein
9 May 2014"""

def pairs (sentence):
    if len(sentence) == 1 or len(sentence) == 0:
        return 0
    if sentence[0] == sentence[1]:
        return 1 + pairs(sentence [2:])
    else:
        return 0 + pairs(sentence[1:])
   
message = input ("Enter a message:\n")
print ("Number of pairs:",pairs(message))