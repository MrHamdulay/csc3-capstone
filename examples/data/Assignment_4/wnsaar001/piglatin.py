def toPigLatin(s):
    temporary=''
    for i in s.split(" "):
        if i[0] in "aeiou":
            temporary+=i+"way "
        else:
            for x in i:
                if x in "aeiou":
                    temporary+=i[i.find(x):]+"a"+i[:i.find(x)]+"ay "
                    break
            else:
                temporary+="a"+i+"ay "           
    return temporary[:len(temporary)-1]
def toEnglish(s):
    temporary=''
    wordy=''
    for i in s.split(" "):
        if i[len(i)-3:] == "way":
            temporary+=i[:len(i)-3]+" "
        else:
            wordy = i[::-1][2:]
            for x in i:
                if x == "a":
                    temporary+=(wordy[wordy.find('a')+1:]+wordy[:wordy.find('a')])[::-1]+' '
                    break
    return temporary[:len(temporary)-1]
