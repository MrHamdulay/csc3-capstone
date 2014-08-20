# BLKAT005
# Kate Bell
# 6 May 2014 

def chr_pairs(s):
    # base cases
    if len(s)==2:
        if s[0]==s[1]:
            return 1
        else: return 0
    if len(s)==1:
        return 0
    #recursive step
    if not s[0]==s[1]:
        return chr_pairs(s[1::])
    if s[0]==s[1]:
        return 1 + chr_pairs(s[2::])
        

sentence = input("Enter a message:\n")
print("Number of pairs:",chr_pairs(sentence))