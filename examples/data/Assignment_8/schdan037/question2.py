"""Daniel schwartz
SCHDAN037
question 2 count pairs
may 2014"""


def count_pairs(s):
    """counts the number of pairs of letters in a string recursively"""
    if s == "" or len(s) == 1:
        return 0
    elif s[0] == s[1]:
        return 1 + count_pairs(s[2:])
    else:
        return 0 + count_pairs(s[1:])


if __name__ == '__main__':
    s = input("Enter a message: \n")
    print("Number of pairs: " + str(count_pairs(s)))