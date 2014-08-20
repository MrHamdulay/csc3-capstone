# Sphiwe Muthembi
# Student Number: MTHSPH007
def toPigLatin(s):
    ans=""
    for word in s.split():
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            ans+=word+"way " #:vowels
        else:
            j=0
            x=word+"a"
            for i in word:
                if i!="a" or i!="e" or i!="o" or i!="u" or i!="i":
                    if i=="a" or i=="e" or i=="o" or i=="i" or i=="u": break
                y=x[j+1:]+x[0]       
                x=y #cons
            ans+=x+"ay "                           
    return ans        
          #============================toEnglish====================
def toEnglish(s):
    ans=""
    for word in s.split():        
        y=len(word)-2
        new_word=word[:y] 
        if new_word[-1]=="w":
            ans+=new_word[:-1]+" " 
        else:
            for i in new_word:
                if new_word[-1]=="a": 
                    ans+=new_word[:-1]+" "
                    break
                else:
                    x=new_word[-1]+new_word[:-1]
                    new_word=x
    return ans
        
