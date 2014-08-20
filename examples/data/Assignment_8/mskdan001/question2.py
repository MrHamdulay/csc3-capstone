"""danson masuka
program to count number of pairs
7 may 2014"""

def counter(c):
    if len(c) == 1:
        return 0
    if c == "":
        return 0
    else:
        if c[0] != c[1]:
            return 0+counter(c[1:])
        else:
            return 1+counter(c[2:])

c =input("Enter a message:\n")
print ("Number of pairs:",counter(c))