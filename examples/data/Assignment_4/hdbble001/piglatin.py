def toPigLatin(s):
    x=s.split(" ")
    sentence=''
    for i in x:
        if i[0] in "aeiou":
            sentence+=i+"way "
        else:
            for j in i:
                if j in "aeiou":
                    sentence+=i[i.find(j):]+"a"+i[:i.find(j)]+"ay "
                    break
            else:
                sentence+="a"+i+"ay "           
    return sentence[:len(sentence)-1]



def toEnglish(s):
    x=s.split(" ")
    sentence=''
    word1=''
    for i in x:
        if i[len(i)-3:] == "way":
            sentence+=i[:len(i)-3]+" "
        else:
            word1 = i[::-1][2:]
            for j in i:
                if j == "a":
                    sentence+=(word1[word1.find('a')+1:]+word1[:word1.find('a')])[::-1]+' '
                    break
    return sentence[:len(sentence)-1]


