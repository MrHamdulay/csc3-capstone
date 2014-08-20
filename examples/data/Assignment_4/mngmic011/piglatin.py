#Micaela Menegaldo
#question3


def toPigLatin (s):
    split_s=s.split(" ")
    new_s=""
    for word in split_s:
        if word[0] in "aeiou":
            PGword=word+"way"  
        elif word[0] not in "aeiou":
            for ch in range(len(word)):
                if word[ch] in "aeiou":
                    sequence=word[0:ch]
                    endletter=len(word)
                    PGword=word[ch:endletter]+"a"+sequence+"ay"
                    break
                else:
                            PGword="a"+word+"ay"                
                    
        new_s+=PGword+" "
    new_s=new_s[:len(new_s)-1]
    return new_s

def toEnglish (s):
    split_s=s.split(" ")
    new_s=""
    for word in split_s:
        if word[len(word)-3:len(word)]=="way":
            Eword=word[0:len(word)-3]
        else:
            Eword=word[0:(len(word)-2)]
            for ch in range(len(Eword),0,-1):
                if Eword[-ch+2]=="a":
                    Eword=(Eword[(-ch+3):(len(Eword))])+(Eword[0:-ch+2])
                    break

                
            
        new_s+=Eword+" "
    new_s=new_s[:len(new_s)-1]
    return new_s