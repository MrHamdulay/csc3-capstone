# Module that contains functions that translate an english word to piglatin vise versa
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 2014/03/29

def seperate(word):
    return word.split(' ')

def checkPig(a):
    k=''
    if a[0] in 'aeiou':
        return a+'way'
    else:
        for i in range(len(a)):
            if a[i] in 'aeiou': break
            else:   k+=a[i]
        return a[len(k):]+'a'+k+'ay'

def checkEng(a):
    k=''
    if a[len(a)-3:len(a)] in 'way':
        return a[:len(a)-3]
    else:
        a=a[:len(a)-2]
        k=''
        i=0
        while a[len(a)-1-i] != 'a':
            k+=a[len(a)-i-1]
            i+=1
        return k[::-1]+a[:len(a)-1-i]

def toPigLatin(s):
    s = seperate(s)
    l = len(s)
    sentence=''
    for i in range(l):
        sentence += checkPig(s[i])
        if i<l-1:
            sentence +=' '
    return sentence

def toEnglish(s):
    s = seperate(s)
    l = len(s)
    sentence=''
    for i in range(l):
        sentence += checkEng(s[i])
        if i<l-1:
            sentence +=' '
    return sentence    