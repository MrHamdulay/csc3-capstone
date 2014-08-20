def toPigLatin(s):
    a=''
    for i in s.split(" "):
        if i[0] in "aeiou":
            a+=i+"way "
        else:
            for x in i:
                if x in "aeiou":
                    a+=i[i.find(x):]+"a"+i[:i.find(x)]+"ay "
                    break
            else:
                a+="a"+i+"ay "           
    return a[:len(a)-1]
def toEnglish(s):
    a=''
    wordy=''
    for i in s.split(" "):
        if i[len(i)-3:] == "way":
            a+=i[:len(i)-3]+" "
        else:
            wordy = i[::-1][2:]
            for x in i:
                if x == "a":
                    a+=(wordy[wordy.find('a')+1:]+wordy[:wordy.find('a')])[::-1]+' '
                    break
    return a[:len(a)-1]
