# Martin Batek
# BTKMAR001
# 2 April 2014
# A program which can translate from piglatin to english and back

def toPigLatin(s):
    def piglatin(a):
        position = 0
        if a[0] == "a" or a[0] == "e" or a[0] == "i" or a[0] == "o" or a[0] == "u" or a[0] == "y":
            return a+"way"
    
        else:
            if len(a) == 1:
                return "a"+a+"ay"
            else:
                while a[position] != "a" and a[position] != "e" and a[position] != "i" and a[position] != "o" and a[position] != "u" and a[position] != "y":
                    position += 1
                    if position > len(a)-1:
                        return "a"+a+"ay"                    
            return a[position:]+"a"+a[:position]+"ay"
    # translates given english word to piglatin
    sentence = s.split(" ")
    x = ""
    for word in sentence:
        x += piglatin(word) + " "
    return x
# uses piglatin() to translate an english sentence to piglatin        
def toEnglish(s):
    def english(a):
        if a[len(a)-3:] == "way":
            return a[:len(a)-3]
        else:
            if len(a) == 5:
                if a [1] == "a" or a[1] == "e" or a[1] == "i" or a[1] == "o" or a[1] =="u":
                    return a[2:0:-1]
                else:
                    return a[1:3]
            elif len(a) == 4:
                return a[1]
            else:
                position = len(a)-3
                while a[position] != "a":
                    position -= 1
                return a[position+1:len(a)-2]+a[:position]
     # Translates a given piglatin word to english   
    sentence = s.split(" ")
    x = ""
    for word in sentence:
        x += english(word) + " "
    return x
# Uses english() to translate given piglatin sentence to english