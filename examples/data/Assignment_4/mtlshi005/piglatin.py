#Piglatin programme
#Shivaan Motilal
#05/04/2014




def toPigLatin(s):
    
    sentence=s.split()
    pig = ''
    
    
    for word in sentence:
        
        if word[0]=='a' or word[0]=='i' or word[0]=='o' or word[0]=='u' or word[0]=='e':
            
            pig += word+'way'+" "
            
        elif word=='b' or word=='bb' or word=='bbb' or word=='bbbbb' or word=='bbbb':
            pig +="a"+word+'ay'+" "
        
            
        else: 
            
            count=0       
            consonants=""
            for letter in word:
                if letter not in "aeiou":
                
                    consonants+=letter
                    count+=1
                
                else: 
                    pig += word[count:]+"a"+consonants+"ay"+" "
                    break
                
    return pig
               


def toEnglish(s):
    sentence=s.split()
    eng=""
    for word in sentence:
        if word[-3:]=='way':
            word=word[:-3]
            eng+= word+" "
        
        #print(word_reverse)
        
        else:
            word=word[:-2]
            word_reverse= word[::-1]
            
            count=0
            consonants=""            
            
            
            for letter in word_reverse: 
                
        
        
                if letter not in "aeiou":
                    consonants+=letter
                    count+=1
                    #print(consonants,count)
            
                else: break
                
            word_reverse=word_reverse[count:]
            #print(word_reverse)
            word=word_reverse[::-1]
            #print(word)
            word=word[:-1]
            eng+=consonants[::-1]+word+" "
            
    return eng          
        
                
        
                    
                    
            
        
    