# This is a Python program that uses a recursive function to count the number of
# pairs of repeated characters in a string.  Pairs of characters cannot overlap.

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 05 May 2014


def check_pairs(string):
    
    if string == "" or len(string) < 2:        
        return 0 # Base case: empty string or string with less that 2 characters    
    elif string[0] == string[1]:        
        return 1 + check_pairs(string[2:]) # Equal pairs found, add 1    
    else:        
        return 0 + check_pairs(string[2:]) # Equal pairs not found
    
    
def main():
    
    phrase = input("Enter a message:\n")
    
    # Count number of pairs in the phrase
    print("Number of pairs:",check_pairs(phrase))


if __name__ == "__main__":
    main()

#Sample I/O:

#Enter a message:
#hello, Salaama
#Number of pairs: 2