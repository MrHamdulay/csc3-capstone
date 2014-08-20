'''Palindromic recursions
Coded by Irfan Habib
2014/05/08'''

def pair(s):
    if s == '':
        return 0
    else:
        if s[0] == s[1:2:]:
            s = s[2::]
            return (1 + pair(s))
        else:
            s = s[1::]
            return pair(s)   
m = pair(input('Enter a message:\n'))
print ('Number of pairs: ' + str(m))            