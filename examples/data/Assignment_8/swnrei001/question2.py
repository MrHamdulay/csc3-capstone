"""Question 2 of Assignment 8
Recursively checks a message string for repeated pairs of characters
SWNREI001
05/05/2014"""

def count_pairs(message, prev):
    """Recursively checks through string message, checking for and counting
    repeated pairs of characters. Previous char is stored in 'prev'"""
    if message == "": # base case is the empty string
        return 0
        """elif prev == "":
        # either a pair was found, or it is the first call of the function
        # set prev equal to first character
        # do next recursion with shortened message string and new prev
        return count_pairs(message[1:], message[0])"""
    else:
        if message[0] == prev:
            # pair found; add 1 to count and set prev = '' in next recursion
            # (prevents overlap of char pairs)
            return 1 + count_pairs(message[1:], "") 
        else:
            return count_pairs(message[1:], message[0])

def main():
    """Main function of modul: gets line from user and outputs number of 
    adjacent pairs"""
    msg = input("Enter a message:\n")
    print("Number of pairs:", count_pairs(msg, ""))

if __name__ == "__main__":
    main()