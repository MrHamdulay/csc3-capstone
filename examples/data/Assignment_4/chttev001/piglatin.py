#Tevin Chetty
#CHTTEV001
#Assignment 4
#piglatin



def chp(s):
    if s[0] in 'aeiouAEIOU':
        return s + 'way'
    else:
        mylow = len(s) + 1
        for i in 'aeiouAEIOU':
            if i in s:
                mylow = min(mylow, s.find(i))
        return s[mylow:] + 'a' + s[:mylow] + 'ay'

def toPigLatin(s):
    return ' '.join(map(chp, s.split()))

def che(s):
    if s[len(s) - 3:] == 'way':
        return s[:len(s) - 3]
    else:
        s = s[:len(s) - 2]
        cur = len(s) - 1
        while s[cur] != 'a':
            cur -= 1
        return s[cur + 1:] + s[:cur] 

def toEnglish(s):
    return ' '.join(map(che,s.split()))
