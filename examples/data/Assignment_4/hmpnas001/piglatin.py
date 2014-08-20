def toPigLatin(s):
    piglatin=''
    sentence=s.split()
    for word in sentence:
        for i in word:
            if i =='a'or i =='e'or i =='i' or i =='o'or i =='u':
                p=word+'way '
                piglatin+=p
                break
            else:
                j=0
                while j<len(word):
                    if word[j]=='a'or word[j]=='e'or word[j]=='i' or word[j]=='o'or word[j]=='u':
                        break
                    j= j+1
                n_word=word[j:]+'a'+word[:j]+'ay ' 
                piglatin+=n_word
                break
    return piglatin

def toEnglish(s):
    english=''
    sentence=s.split()
    for word in sentence:
        if word[-3:] == 'way':
                k=word[:-3]
                english+=k+' '
            
        else:
            k=word[:-2]
            for j in range(len(k)-1,0,-1):
                if s[j]=='a':
                    break
                
            t=k[j+1:]+k[:j]
            english+=t+' '
    return english     
