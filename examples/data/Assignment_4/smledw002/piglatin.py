__author__ = 'User1'
import string
from string import *

def to_PigLatin(x):
    if x[0].lower() in "aeiou":
        x = str(x) + "way"
        return x
    else:
        lowest = len(x)
        for i in "aeiou":
            y = x.lower()
            if lowest> y.find(i) and y.find(i) != 0 and y.find(i) != -1:
                lowest=y.find(i)

        if y:
            x = x[lowest:] + "a" + x[:lowest] + "ay"
            return x



def to_English(x):
    if x[-3:] == "way":
        return x[0:-3]
    elif x[-2:].lower() == "ay":
        x= x[0:-2]
        counter = 0
        for i in x[::-1]:
            counter += 1
            if i == "a":
                break
        counter *= -1
        x = x[counter+1:] + x[:counter]
        return x
def toPigLatin(x):
    words = x.split(" ")
    sente =""
    for word in words:
        sente = sente +" "+ to_PigLatin(word)
    return sente[1:]

def toEnglish(x):
    words = x.split(" ")
    sente =""
    for word in words:
        sente = sente +" "+ to_English(word)
    return sente[1:]

