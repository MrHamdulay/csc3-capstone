''' SANELE MLALOSE
    ASSIGNMENT4,QUESTION3
    English to PigLatin and vise versa'''

def toPigLatin(s):
    separate=s.split(' ')
    new_s=""
    for i in range(len(separate)):
        sep_word=separate[i]
        if sep_word[0] in 'aeiou':
            sep_word=sep_word+"way"
    
        else:
            vowelPresent=False
            for j in range(1,len(sep_word)):
                if sep_word[j] in 'aeiou':
                    sep_word=sep_word[j:]+'a'+sep_word[0:j]+"ay"
                    vowelPresent=True
                    break
            if (vowelPresent==False):
                sep_word='a'+sep_word+'ay'
      
            sep_word=sep_word+''
            
        
        new_s+=sep_word+" "                          
    return new_s
    
def toEnglish(s):
    separate=s.split(' ')
    new_s=''
    for i in range(len(separate)):
        sep_word=separate[i]
        if sep_word[-3::1]=="way":
            sep_word=sep_word[:-3]
            
        else:
            if sep_word[-2::1]=="ay":
                sep_word=sep_word[0:-2]
                for c in range(len(sep_word)-1,-1,-1):
                    if sep_word[c]=="a":
                        sep_word=sep_word[c+1:]+sep_word[0:c]
                        break
            sep_word=sep_word+''
            
        new_s+=sep_word+' '
    return new_s    

