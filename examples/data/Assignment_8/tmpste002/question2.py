""" Recursive function to count the number of pairs of repeated characters in a string """
__author__ = 'Stephen Temple'
__date__ = '2014/05/05'


def count_pairs(s) -> int:
    """ Count the number of pairs of repeated characters in a string """
    if len(s) == 1:
        return 0
    elif len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    elif s[0] == s[1]:
        return 1 + count_pairs(s[2:])
    else:
        return count_pairs(s[1:])


if __name__ == '__main__':
    string = input("Enter a message:\n")
    print("Number of pairs: "+ str(count_pairs(string)))