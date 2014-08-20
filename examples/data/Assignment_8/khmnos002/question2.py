"""program to count number of pairs of repeated characters in a string
nosipho khumalo
04 May 2014"""


def count_repeat(word):
    if len(word) <= 1:
        return 0
    elif len(word) == 2:
        if word[0] == word[1]:
            return 1
        else:
            return 0
    elif word[0] == word[1]:
        return 1 + count_repeat(word[2:])
    else:
        return 0 + count_repeat(word[1:])

word = input("Enter a message: \n")
print("Number of pairs:", count_repeat(word))