v='aeiouAEIOU'

v='aeiouAEIOU'
def PigLatin(s):
    for i in range(len(s)):
        if v.find(s[i])!=-1:
            vowel=True
            break
        else:
            vowel=False
    
    if vowel:
        if len(s)>2:
            x=s[0]
            y=s[1]
            place=1
            
            if v.find(x)!=-1:
                    answer=s+'way'
                    return answer
            else:
                    for i in range(len(s)):
                    
                            if v.find(y)==-1:
                                    y=s[i+2]
                                    place+=1
                            else:
                                    newS=s[place:]
                                    begS=s[:place]
                                    answer=newS+'a'+begS+'ay'
        else:
            if v.find(s[0])!=-1:
                                    answer=s+'way'
                                    return answer    
            else:                
                    if len(s)==1:
                            answer='a'+s+'ay'
                    elif len(s)==2:
                            if v.find(s[1])==-1:
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
                        place=word.find(' ')
                        letter=word[:place]
                        Pig=PigLatin(letter)+' '
                        answer=answer+Pig
                        word=word[(place+1):]
                else:
                        first=word
                        Pig=PigLatin(first)
                        answer=answer+Pig
                        break
        
        return answer
                
def Convert(s):
        place='0'
        if s[-3]=='w':
                answer=s[:-3]
                return answer
        else:
                word=s[:-2]
                bword=word[::-1]
                place=bword.find('a')
                word1=bword[:place]
                word2=bword[place+1:]
                new_word=word2+word1
                answer=new_word[::-1]
                return answer
                
def toEnglish(s):
        word=s
        place=0
        answer=''
        while True:
        
                if word.find(' ')!=-1:
                        place=word.find(' ')
                        letter=word[:place]
                        New=Convert(letter)+' '
                        answer=answer+New
                        word=word[(place+1):]
                else:
                        letter=word
                        New=Convert(letter)
                        answer=answer+New
                        break
        
        return answer