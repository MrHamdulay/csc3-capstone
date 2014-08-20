"""Program to check for paired letters in a string
Runako Muzwidzwa
06/05/2014"""
v=input("Enter a message:\n")
def pairs(v):
    if len(v)<2:
        return 0 #to return  number
    elif v[0] == v[1]:
        n=v[2:]
        return 1 + pairs(n)
    else:
        return pairs(v[1:])#calls function with the message after slicing
print("Number of pairs:",pairs(v))