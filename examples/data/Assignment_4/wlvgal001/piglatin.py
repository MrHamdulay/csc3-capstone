#Galya Wolov
#Pig Latin to English and vice versa Translator
#1/4/2014
def toPigLatin(s):
    string=''
    for i in s.split(' '):
        if i[0] in 'aeiou':
            string+=i+'way ' #begins with vowel gets way
        else:
            for j in i:
                if j in 'aeiou':
                    string+=i[i.find(j):]+'a'+i[:i.find(j)]+'ay ' #or else starts with consonant group gets a after then consonant conglomerate then ay at end
                    break #get to what you need stop iterating loop
            else:
                string+='a'+i+'ay '            
    return string[:len(string)-1]
def toEnglish(s):
    string=''
    revstring=''
    for i in s.split(" "):
        if i[len(i)-3:] == 'way':
            string+=i[:len(i)-3]+' '
        else:
            revstring = i[::-1][2:]
            for p in i:
                if p == 'a':
                    string+=(revstring[revstring.find('a')+1:]+revstring[:revstring.find('a')])[::-1]+' '
                    break
    return string[:len(string)-1]
