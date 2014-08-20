def toPigLatin(s):
    word=''
    for j in s.split(" "):
        if j[0] in "aeiou":
            word+=j+"way "
        else:
            for x in j:
                if x in "aeiou":
                    word+=j[j.find(x):]+"a"+j[:j.find(x)]+"ay "
                    break
            else:
                temp+="a"+j+"ay "           
    return word[:len(word)-1]
def toEnglish(s):
    word=''
    temp=''
    for i in s.split(" "):
        if i[len(i)-3:] == "way":
            temp+=i[:len(i)-3]+" "
        else:
            word = i[::-1][2:]
            for x in i:
                if x == "a":
                    temp+=(word[word.find('a')+1:]+word[:word.find('a')])[::-1]+' '
                    break
    return temp[:len(temp)-1]
