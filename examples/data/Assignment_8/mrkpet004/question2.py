"""program that uses a recursive function to count the number of pairs of repeated characters in a string
peter m muriuki
9/5/14"""

string=input("Enter a message:\n")
a="Number of pairs:"
def n_pairs(string):
     # base case - empty string
    if len(string)==0:
        return 0
    # first step-for single character in string 
    if len(string)==1:
        return n_pairs(string[1:])
    # second recursive step - check for alphabetic letters,if found increment count for number of pairs
    elif string[0]==" " or string[0]==",":
        return n_pairs(string[1:])
    # if alphabetic,compare first and second characters and increase count if similar
    else:
        if string[0]==string[1]:
            return 1 + n_pairs(string[2:])
        else:
            return n_pairs(string[1:])

print(a,n_pairs(string))