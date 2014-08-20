'''question2.py
count the number of unoverlapped pairs in a string using recursion
douglas newton NWTDOU001
9 may 2014'''

def num_pairs(s):
    if len(s)<2:
        return 0
    if s[0]==s[1]:
        return 1 + num_pairs(s[2:])
    return num_pairs(s[1:])

# get input from user
string = input('Enter a message:\n')

print('Number of pairs:',num_pairs(string))