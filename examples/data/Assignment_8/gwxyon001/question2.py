''' identify pairs of repeated characters
Yongama Giwu
05/08/2014'''
def pair_id(s):
    if len(s)<2:
        return 0
    elif s[0] == s[1]:
        return 1 + pair_id(s[2:])
    else:
        return pair_id(s[1:])
message=input("Enter a message:\n")
print("Number of pairs:",pair_id(message))