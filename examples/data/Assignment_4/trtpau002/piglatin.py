#PigLatin-English
#Paul Truter
#04 April 2014

vowels=('a','e','i','o','u')

def toPigLatin(sentence):
    words=sentence.split()
    for word in words:
        firstLetter=word[0]
        secondLetter=word[1]
        thirdLetter=word[2]
        if firstLetter in vowels:
            print(word + "way",end=" ")        
        elif secondLetter in vowels:
            print(word[1:] + "a" + word[0] + "ay",end=" ")
        elif thirdLetter in vowels:
            print(word[2:] + "a" + word[0] + word[1] + "ay",end=" ")
        else:
            print(word[3:] + "a" + word[0] + word[1] + word[2] + "ay",end=" ")


def toEnglish(sentence):
    words=''
    y=''
    for i in sentence.split():
        if i[len(i)-3:] == "way":
            words+=i[:len(i)-3]+" "
        else:
            y = i[::-1][2:]
            for x in i:
                if x == "a":
                    words+=(y[y.find('a')+1:]+y[:y.find('a')])[::-1]+' '
                    break
    return words[:len(words)-1]
    
                
            

            