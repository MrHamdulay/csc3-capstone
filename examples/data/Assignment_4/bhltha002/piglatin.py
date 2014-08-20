my_vowels='aeiouAEIOU'

my_vowels='aeiouAEIOU'
def PigLatin(s):
    for i in range(len(s)):
        if my_vowels.find(s[i])!=-1:
            vowel=True
            break
        else:
            vowel=False
    
    if vowel:
        if len(s)>2:
                        x=s[0]
                        y=s[1]
                        position=1
                        
                        if my_vowels.find(x)!=-1:
                                answer=s+'way'
                                return answer
                        else:
                                for i in range(len(s)):
                                
                                        if my_vowels.find(y)==-1:
                                                y=s[i+2]
                                                position+=1
                                        else:
                                                newS=s[position:]
                                                begS=s[:position]
                                                answer=newS+'a'+begS+'ay'
        else:
                        if my_vowels.find(s[0])!=-1:
                                                answer=s+'way'
                                                return answer    
                        else:                
                                if len(s)==1:
                                        answer='a'+s+'ay'
                                elif len(s)==2:
                                        if my_vowels.find(s[1])==-1:
                                                answer='a'+s+'ay'
                                        else:
                                                answer=s[1]+'a'+s[0]+'ay'
    else:
        answer='a'+s+'ay'
        
    return answer
    
           
def toPigLatin(s):
        word=s
        position=0
        answer=''
        while True:
        
                if word.find(' ')!=-1:
                        position=word.find(' ')
                        first=word[:position]
                        Pig=PigLatin(first)+' '
                        answer=answer+Pig
                        word=word[(position+1):]
                else:
                        first=word
                        Pig=PigLatin(first)
                        answer=answer+Pig
                        break
        
        return answer
                
def English(s):
        position='0'
        if s[-3]=='w':
                answer=s[:-3]
                return answer
        else:
                word=s[:-2]
                backward=word[::-1]
                position=backward.find('a')
                word_one=backward[:position]
                word_two=backward[position+1:]
                new_word=word_two+word_one
                answer=new_word[::-1]
                return answer
                
def toEnglish(s):
        word=s
        position=0
        answer=''
        while True:
        
                if word.find(' ')!=-1:
                        position=word.find(' ')
                        first=word[:position]
                        Pig=English(first)+' '
                        answer=answer+Pig
                        word=word[(position+1):]
                else:
                        first=word
                        Pig=English(first)
                        answer=answer+Pig
                        break
        
        return answer        