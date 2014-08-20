# Lehlogonolo Masetla
# CSC 1015F

def countPairs(s):
    if len(s) < 2:
        
        return 0
    elif s[0] == s[1]:
       
        return 1 + countPairs(s[2:])
    else:
    
        return countPairs(s[1:])

msg = input("Enter a message:\n")
print("Number of pairs: ",countPairs(msg),sep='')