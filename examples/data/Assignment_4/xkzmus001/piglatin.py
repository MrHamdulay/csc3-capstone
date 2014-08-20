"""piglatin.py
Author : Musa Xakaza
Date : 01/04/2014"""

def isVowel(word):
    if word[0] in "aeiou" or word[0] in "AEIOU":
        return True
    else:
        return False
    
def endsWay(word):
    reverse = word[::-1]
    if reverse[0:3] == "yaw":
        return True
    else : return False
    
def getConsWord(word):
    flag = False
    lastCons, i = 0, 0
    
    while i < len(word) and not flag:
        if not isVowel(word[i]):
            lastCons = i
            i += 1
        else:
            break
    
    return word[(lastCons+1):]+"a"+word[0:lastCons+1]+"ay"
    
def toPigLatin(s):
    newS = ''
    for word in s.split(' '):
        if isVowel(word):
            newS += " "+word+"way"
        else:
            newS += " "+getConsWord(word)
    
    return newS[1:]
    
def getConsWord2(word):
    reverse = word[::-1]
    pos = reverse.find('a')
    start = reverse[0:pos]
    latter = reverse[(pos+1):]
    return start[::-1]+latter[::-1]

def toEnglish(s):
    newS = ''
    for word in s.split(' '):
        if endsWay(word):
            newS += ' '+word[:-3:]
        else:
            newS += ' '+getConsWord2(word[:-2:])
    return newS[1:]