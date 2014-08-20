def toPigLatin(s):
    temp=''
    for i in s.split(" "):
        if i[0] in "aeiou":
            temp+=i+"way "
        else:
            for x in i:
                if x in "aeiou":
                    temp+=i[i.find(x):]+"a"+i[:i.find(x)]+"ay "
                    break
            else:
                temp+="a"+i+"ay "           
    return temp[:len(temp)-1]
def toEnglish(s):
    temp=''
    wordy=''
    for i in s.split(" "):
        if i[len(i)-3:] == "way":
            temp+=i[:len(i)-3]+" "
        else:
            wordy = i[::-1][2:]
            for x in i:
                if x == "a":
                    temp+=(wordy[wordy.find('a')+1:]+wordy[:wordy.find('a')])[::-1]+' '
                    break
    return temp[:len(temp)-1]
