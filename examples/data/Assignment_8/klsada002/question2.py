"""Adam Kaliski
CSC1015F Assignment 8 Q2
2014-05-08"""
num=0
def numDistchars(strng):
    global num
    if strng == '':
        print('Number of pairs:',num)
        return 0
    else:
        if strng[0:1] == strng[1:2]:
            num+=1
            numDistchars(strng[2:])
        else:
            numDistchars(strng[1:])
word = input("Enter a message:\n")
numDistchars(word)