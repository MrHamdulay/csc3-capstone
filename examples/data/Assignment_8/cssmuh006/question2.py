"""count pair of characters in a string
Haaroon Cassiem
8 May 2014"""
def count_pairs(l):
    #count number of pairs in a string
    if l=="":
        return 0
    elif len(l)>1 and (l[0]==l[1]):
        return 1+count_pairs(l[2:])
    else:
        return count_pairs(l[2:])

#call functions
if __name__=="__main__":
    m=input("Enter a message:\n")
    print("Number of pairs:",count_pairs(m))