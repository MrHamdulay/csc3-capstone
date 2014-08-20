def toPigLatin(s):
    listWords = s.split()
    for x in range (0, len(listWords)):
        vowelFound = False
        cString = ""
        counter = 0
        while (vowelFound == False and counter < len(listWords[x])):
            if (listWords[x][counter] in "aeiou"):
                vowelFound = True
            else:
                cString += listWords[x][counter]
                counter += 1
        if (counter == 0):
            listWords[x] = listWords[x] + "way"
        else:
            listWords[x] = listWords[x][counter:] + "a" + cString + "ay"
    return " ".join(listWords)

def toEnglish(s):
    listWords = s.split()
    for x in range (0, len(listWords)):
        if (listWords[x][-3] == "w"):
            listWords[x] = listWords[x][0: -3]
        else:
            index = listWords[x].rfind("a", 0, len(listWords[x]) - 3)
            listWords[x] = listWords[x][index+1:len(listWords[x])-2] + listWords[x][0:index]
    return " ".join(listWords)