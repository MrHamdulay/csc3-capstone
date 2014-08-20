"""program to find string pairs
chris betteridge
06 may 2014"""

def pairs(string):
    #base case testing - check if not long enough to have pairs  
    if len(string) == 1 or len(string) == 0:
        return 0
    #test to see if index one and two are equal, then iterate
    if string[0] == string[1]:
        return 1 + pairs(string[2:])
    else:
        return pairs(string[1:])
string = input("Enter a message:\n")
print("Number of pairs:",pairs(string))
