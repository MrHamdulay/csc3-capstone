"""
Prashanth Sridharan
SRDPRA001
Assignment 4
piglatin
"""
def toPigLatin(s):
    s1=""
    for word in s.split():
        if word[0] in "aeiou":
            s1+=word + "way "
        else:
            consInd = 0
            boo = False
            for j in range(0,len(word)):
                if word[j] in "aeiou":
                    boo = True
            if(boo):
                for i in range(0,len(word)):
                    if word[i] in "aeiou":
                        consInd = i-1
                        break
                s1+=word[i:] + "a" + word[:i] + "ay "
            else:
                s1+= "a"+word+"ay "
    return s1
            
def toEnglish(s):
    s1=""
    for word in s.split():
        if word[-3:]=="way":
            s1+=word[:-3]+" "
        else:
            consInd=0
            for i in range(len(word)-3, -1,-1):
                if word[i] in "aeiou":
                    consInd = i
                    break
            s1+=word[i+1:len(word)-2]+word[:i]+" "
    return s1     