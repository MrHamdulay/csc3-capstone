#question2
#author: justin valsecchi

def countPairs(s):
    if len(s) == 1: #Base case
        return 0
    elif len(s) == 2:
        if s[0] == s[1]: #compares char '1', to one after
            return 1 # returns a value 1
        else:
            return 0
    elif s[0] == s[1]: #repeats the process in base case
        return 1 + countPairs(s[2:]) # adds 1 to the previous value of countPairs
    else:
        return countPairs(s[1:])# returns value to the previous value of countpairs


string = input("Enter a message:\n")
print("Number of pairs: "+ str(countPairs(string)))