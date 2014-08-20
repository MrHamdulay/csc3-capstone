# Tayla Radmore
# 6 May 2014
# finding pairs of letters

def repeats (s):
    
    
    if len (s) == 1 or len(s) == 0 :
        return 0
    
    elif s[:1] == s[1:2]:
        return 1 + repeats(s[2:])
    
    else:
        return 0 + repeats (s[1:])
s=input("Enter a message:\n")
print("Number of pairs:",repeats(s))
