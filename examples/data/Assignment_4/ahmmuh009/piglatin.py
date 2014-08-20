def toEnglish(s):
    string=s.split()
    eng_string=""
    for i in range(len(string)):
        if string[i][-3:]=='way':
            eng_string+=string[i][:-3]+" "
        elif string[i][-2:]=='ay':
            part_word=string[i][:-2]
            rem_a=part_word.rfind('a')
            eng_string+=part_word[rem_a+1:]+part_word[:rem_a]+" "
    return eng_string


def toPigLatin(s):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U") 
    words =  s.split()  
    count = 0
    string=""
    for word in words:
        count=0
        consonants=""
        if word[0:1] in vowels:
            string+=word+"way "
        elif len(word)==1 and word[0] not in vowels:
            string+="a"+word+"ay" 
        else:
            count=0        
            while word[count] not in vowels:
                consonants +=word[count]
                count+=1
                if word[count] in vowels:
                    break
            string+=word[count:]+"a" +consonants +'ay '
    return string


