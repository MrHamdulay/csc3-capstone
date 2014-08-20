#Assignment 4
#Question 3
#Barry Su
#2 April 2014

import math

vowel=["a","e","i","o","u"]

def no_vowel(x):
    wordsplit=list(x)
    letter_count=len(wordsplit)
    count=0
    checker=0
    for i in range(letter_count):
        if wordsplit[count] in vowel:
            checker=1
        count=count+1
    if checker==1:
        none=""
        return none
    
    if checker==0:
        word="a"+x+"ay "
        return word


def toPigLatin(s):
    separate=s.split(" ")
    count=s.count(" ")
    count=count+1
    
    loop_count=0
    new_s=""
    for i in range(count):
        wordsplit=list(separate[loop_count])
        wordcounter=len(wordsplit)
        
        NoVowels=no_vowel(separate[loop_count])
        new_s=new_s+NoVowels 
    
        
        if wordsplit[0] in vowel:
            new_w=separate[loop_count]+"way "
            new_s=new_s+new_w
        else:
            counter=0
            for j in range(wordcounter):
                if wordsplit[counter] in vowel:
                    new_w=(separate[loop_count])[0:counter]
                    word=(separate[loop_count])[counter:]+"a"+new_w+"ay "
                    new_s=new_s+word 
                    break
                counter=counter+1
        loop_count=loop_count+1
        
    return new_s
    
def toEnglish(s):
    separate=s.split(" ")
    count=s.count(" ")
    loop_count=0
    new_s=""
    for i in range(-1,count):
        wordsplit=list(separate[loop_count])
        wordcounter=len(wordsplit)   
        
        if (separate[loop_count])[wordcounter-3:]=="way":
            new_w=(separate[loop_count])[0:wordcounter- 3]
            new_s=new_s+new_w+" "
        else:
            if (separate[loop_count])[wordcounter-2:]=="ay":
                remove_AY=(separate[loop_count])[0:wordcounter-2]
                PosA=remove_AY.rfind("a")
                consonant=remove_AY[PosA+1:wordcounter-2]
                word=remove_AY[0:PosA]
                eng_word=consonant+word
                new_s=new_s+eng_word+" " 
        loop_count=loop_count+1
    return new_s
                    
           
           
    
           
                
                
                
    