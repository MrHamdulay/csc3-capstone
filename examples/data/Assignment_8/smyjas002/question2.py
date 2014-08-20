#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 8
#question 2

def numPairs (testStr):
    # base case, 
    if len (testStr) < 2:
        return 0
    # first recursive step, tests if first two letters are a pair
    elif testStr[0] == testStr[1]:
        return 1 + numPairs (testStr[2:])
    # second recursive step, if letters are not a pair
    else:
        return 0 + numPairs (testStr[1:])

def main():
	a = input("Enter a message:\n")
	print("Number of pairs:", numPairs(a))

main()
"""
 Sample I/O:

Enter a message:
hello, Salaama
Number of pairs: 2
"""
