from functools import reduce

vw = "aeiou"
vww = "aeiouw"

def wordToPigLatin(s):
    pos = reduce(min, map(lambda x: s.find(x) if s.find(x) > -1 else 666, vw))
    return s + "way" if pos == 0 else s[pos:] + "a" + s[:pos] + "ay"

def wordToEnglish(s):
    pos = len(s)-3-reduce(min, map(lambda x: s[::-1][2:].find(x) if s[::-1][2:].find(x) > -1 else 666, vww))
    return s[pos+1:-2] + s[:pos] if s[pos:-2] != "w" else s[:pos]

def toPigLatin(s):
    return reduce(lambda x, y: x+" "+y, map(wordToPigLatin, s.split(" ")))

def toEnglish(s):
    return reduce(lambda x, y: x+" "+y, map(wordToEnglish, s.split(" ")))
