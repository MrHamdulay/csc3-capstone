"""Program which counts the numbers of pairs of repeated characters
Khanyisile Morudu
06 May 2014"""

#input
message = input("Enter a message:\n")

#recursive function
def Num_pairs(s):
    #if the string is less than 1, then there is nothing to compare it to
    if len(s) < 2:
        return  0
    #checking if there are pairs are there
    elif s[0] == s[1]:
        return 1 + Num_pairs(s[2:len(s)])
    else :
        return Num_pairs(s[1:len(s)])
#output
print("Number of pairs:", Num_pairs(message)) 
