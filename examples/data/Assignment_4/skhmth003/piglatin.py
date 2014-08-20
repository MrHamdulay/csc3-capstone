def vowel (word):
    global vow_prop
    global count
    if word == "a" or word == "e" or word == 'i' or word == "o" or word == "u":
        vow_prop = True
    elif word == False:
        vow_prop = False
    elif not(word[0] == "a" or word[0] == "e"or word[0] == "i" or word[0] == "o" or word[0] == "u"):
        if not(len(word)) == 1:
            vowel(word[1:])
        else:
            vow_prop = False
    else:
        vow_prop = True
    return vow_prop
    
def toPigLatin (x):
    pig_sen = ""
    x_array = x.split(" ")
    for i in x_array:
        prefix = ""
        if (i[0] == "a" or i[0] == "e" or i[0] == "i" or i[0] == "o" or i[0] == "u"):
            i = i+"way"
            pig_sen += i + " "

        elif (vowel(i) == True):
                count=0
                while i[count]!="i" and i[count]!="a" and i[count]!="e" and i[count]!="u" and i[count]!="o":
                    count+=1
                prefix=i[0:count]
                pig_sen+=i[count:]+"a"+prefix+"ay"+" "
        else:
            pig_sen += "a" + i + "ay "

    return pig_sen[:len(pig_sen)-1]

def toEnglish (x):
    eng_sen = ""
    cons_word = ""
    prefix = ""
    x_array = x.split(" ")
    rev_array = []
    for i in x_array:
        rev_array.append(i[::-1])
    for j in rev_array:
        if (j[:3] == "yaw"):
            x_j = j[::-1]
            eng_sen += x_j[0:len(j)-3] + " "
        else:
            x_j = j[::-1]
            cons_word = x_j[0:len(j)-2]
            point = cons_word.rfind("a")
            prefix = cons_word[point+1:]
            eng_sen += prefix + cons_word[:point] + " "
    return eng_sen [:len(eng_sen)-1]
