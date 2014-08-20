"""this program finds adjacent identical letters within a phrase or word and determines the number of these pairs of letters
quincy cele
9 may 2014"""
x=input("Enter a message:\n")
def pair_find(string):
    """this function finds pairs of adjacent identical letters"""
    if len(string)<=1:
        return 0
    elif string[0]==string[1]:
        return 1+pair_find(string[2:])
    else:
        return pair_find(string[1:])
#display the number of pairs
y=pair_find(x)
print("Number of pairs:",y)