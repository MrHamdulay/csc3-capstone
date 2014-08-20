def toPigLatin (s):
    sent = s.split()
    pig = ""
    for i in sent:
        if i[0] in "aeiou":
            pig = pig + i + "way" + " "
        else:
            a = 0
            for j in i:
                if j in "aeiou":
                    break
                a = a+1
            y = i[a:]
            z = i[:a]
            pig = pig + y + "a" + z + "ay" + " "
    return pig

def toEnglish (s):
    sent = s.split()
    english = ""
    for i in sent:
        if i[-3:] =="way":
            i = i[:-3]
            english = english + i + " "
        else:
            i = i[:-2]
            x = len(i)-1
            for j in i[::-1]:
                if j =="a":
                    break
                x = x-1
            y = i[x+1:]
            z = i[:x]
            english = english + y + z + " "
    return english