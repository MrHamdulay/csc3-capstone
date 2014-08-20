#Nikhil Jiten Naik
#NKXNIK003

vowels = "aeiou"
def toPigLatin(splitter):
    display= ""
    splitter = splitter.split()
    for i in splitter:
        index = len(i) + 1
        if i[0] in vowels:
            display += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowels:
                    index = j
                    break
            display += i[index:] + "a" + i[:index] + "ay"
        display += " "
    return display
def toEnglish(splitter):
    display = ""
    index = 0
    splitter = splitter.split()
    for i in splitter:
        if i[-3] == "w":
            display += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            display += i[index+1:-2] + i[:index]
        display += " "
    return display