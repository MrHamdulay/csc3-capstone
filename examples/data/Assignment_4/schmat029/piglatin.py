#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     28-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def toPigLatin(s):
    string = s.split()
    piglatin = ""
    for substring in string:
        attach = ""
        for i in substring:
            if i in "aeiou":
                if not attach:
                    piglatin += substring + "way "
                else:
                    piglatin += substring + "a" + attach + "ay "
                break
            else:
                attach += i
                substring = substring[1:]
        else:
            piglatin += "a" + attach + "ay"
    return(piglatin)

def toEnglish(s):
    string = s.split()
    english = ""
    for substring in string:
        if substring[-3] == "w":
            english += substring[:-3] + " "
        else:
            substring = substring[:-2]
            for i in substring:
                if substring[-1] == "a":
                    english += substring[:-1] + " "
                    break
                else:
                    substring = substring[-1] + substring[:-1]
    return english