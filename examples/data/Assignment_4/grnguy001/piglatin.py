def toPigLatin (s):
    sentence=''
    words=s.split(' ')
    for i in words:
        if (i[0] in "AEIOUaeiou"):
            sentence=sentence+i+"way "
        else:
            for j in range(len(i)):
                if (i[j] in "AEIOUaeiou"):
                    m=j
                    break
                else:
                    m=0
            if m==0:
                sentence=sentence+"a"+i+"ay "            
            else:
                sentence=sentence+i[m:]+"a"+i[0:m]+"ay "
                
                
    return sentence[:-1]

def toEnglish (s):
    string=""
    
    for word in s.split(' '):
        if "w" in word:
            string+=word[:-3]+' '
        else:
            word=word[:-2]
            for pos in range(len(word)-1,-1,-1):
                if word[pos]=='a':
                    break
            if pos!=(len(word)+1) or len(word)==3:
                string+=word[pos+1:]+word[:pos]+' '
            elif word=="eath":
                string+="the "
            else:
                string+=word[1:]+" "
                        
            
           
    return string[:-1]
toEnglish("aBbay")