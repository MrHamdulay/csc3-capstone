# Student Number: PRTNIC017
# Date: 5/9/14


def count_pairs(s: list):
    if len(s) <= 1:
        return 0
    else:
        if s[0] == s[1]:
            s.remove(s[0])
            s.remove(s[0])
            return 1 + count_pairs(s)
        else:
            s.remove(s[0])
            return count_pairs(s)


into = list(input('Enter a message:\n'))
print('Number of pairs:', count_pairs(into))