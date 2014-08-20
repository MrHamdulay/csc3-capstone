
def toPigLatin(s):
    s=s.split(' ')
    new=''

    for i in range(len(s)):
        if s[i][0] in 'aeiou':
            s[i]=s[i] + "way"
        elif s[i][0] not in "aeiou":
            s[i]+= "a"
            while s[i][0] not in "aeiou":

                s[i] = s[i][1::] + s[i][0]
            s[i]+= "ay"
        new += s[i]+" "
    return new

def toEnglish(s):
    s=s.split(" ")
    new=""

    for i in range(len(s)):
        if s[i][-3::] == "way":
            s[i]= s[i][:-3]

        if s[i][-2::] == "ay":
            s[i]=s[i][:-2]
            while s[i][-1] not in "aeiou":
               s[i]= s[i][-1] + s[i][:-1]
            s[i]= s[i][:-1]
        new +=s[i]+" "
    return new


