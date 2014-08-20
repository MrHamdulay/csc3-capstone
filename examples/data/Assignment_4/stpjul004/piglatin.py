""" Question 3 | Assignment 4
 Author: Julius Stopfrth (STPJUL004)
 Date: 28/03/2014 """

def toPigLatin(englishString):
    englishString = englishString.strip()
    piglatinString = ''
    words = englishString.split(' ')
    for i in words:
        for j in range(len(i)):
            if j == 0 and i[j] in ['a','e','i','o','u']:
                piglatinString += i + 'way'
                break
            elif (i[j] in ['a','e','i','o','u']):
                piglatinString += i[j:] + 'a' + i[:j] + 'ay'
                break
            elif j == len(i)-1:
                piglatinString += 'a' + i + 'ay'
                break
        piglatinString += ' '
    piglatinString = piglatinString.strip()
    return piglatinString

def toEnglish(piglatinString):
    piglatinString = piglatinString.strip()
    englishString = ''
    prefix = ''
    words = piglatinString.split(' ')
    for i in words:
        i = i[:len(i)-2]
        prefix = ''
        for j in i[::-1]:
            ndx = i[::-1].index(j) + 1
            if j == 'w' or j == 'a':
                englishString += prefix[::-1] + i[:len(i)-ndx]
                break
            else:
                prefix += j
        englishString += ' '
    englishString = englishString.strip()
    return englishString