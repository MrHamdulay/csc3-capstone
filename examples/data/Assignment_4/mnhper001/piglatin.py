def toPigLatin(english_sentence):
    english_sentence
    word=""
    start=0
    end=0
    track=0
    length=len(english_sentence)-1
    for i in english_sentence:
        if i!=" " and track!=length:
            end+=1
            track+=1
        else:
            if (track ==length):
                word1=english_sentence[start:]
            else:
                word1=english_sentence[start:end]
            end+=1
            first_letter=word1[0].lower()
            vowels="aeiou"
            if first_letter in vowels:
                word1=word1+"way"
                word+=word1+" "
            else:
                word1=word1+"a"
                count=0
                for j in word1:
                    if j.lower() in vowels:
                        break
                    count+=1
                word1= word1[count:]+word1[:count]+"ay"
                word+=word1+" "
            start=end
            track+=1
        
    return word

def toEnglish(latin_sentence):
    word=""
    start=0
    end=0
    track=0
    length=len(latin_sentence)-1
    for i in latin_sentence:
        if i!=" " and track!=length:
            end+=1
            track+=1
        else:
            if (track ==length):
                word1=latin_sentence[start:]
            else:
                word1=latin_sentence[start:end]
            end+=1
            trial=word1[:len(word1)-3]
            if word1[len(word1)-3:]=="way":
                word1=word1[:len(word1)-3]
                word+=word1+" "
            else:
                word1=word1[:len(word1)-2]
                test=word1[::-1]
                count=0
                for j in test:
                    if j.lower()=="a":
                        break
                    if (j.lower()!="a"):
                        word1=j+word1
                    count+=1
                word1= word1[:len(word1)-count-1]
                word+=word1+" "
            start=end
            track+=1
        
    return word




            
            
       
        
        
                   
    