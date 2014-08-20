'''pairs of repeated letters program
Adam Oosthuizen OSTADA001'''

def checkPairs(s):
    
    if len(s) >= 2:
        if s[0] == s[1]:
            #if len(s[2:len(s)])>2:
                return 1 + checkPairs(s[2:len(s)])
        else:
            #if len(s[1:len(s)])>2:    
                return checkPairs(s[1:len(s)])
  
    else:
        return 0

s = input("Enter a message:\n")

print("Number of pairs:",checkPairs(s))