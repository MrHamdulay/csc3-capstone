#PigLatin program
 
def toPigLatin (s):
   
    words = s.split()      
    result = ''
    for word in words:
        
        if word[0] in 'aeiou':
            result =result+word +'way'+' ' 
             
        
        else:
            pos=0
            for i in range(len(word)):
                if word[i] in 'aeiou':
                    pos = i
                    break
            if pos == 0:
                
                result = result +'a'+ word+'ay '
            else:
                result = result + word[pos::] +'a'+ word[0:pos:]+'ay '
            
    return result[:-1]
            
            
    
            
    

def toEnglish (s):
    
    words = s.split()
    result = ''
    
    for word in words:
        
        if word[-3:] == 'way':
            result = result + word[:-3]+ ' '
            
        else:
            
            
            endWord = word[:-2]
            pos = endWord.rfind('a')
          #  print (pos)
            
            last = endWord[pos+1:]
            printword=endWord[:pos]
           # print(printword)
            #print (last) 
            result = result+last+printword+' '
            
           # result = result + word [:pos] + word[:-2]+' '

                   
            
            
    return result[:-1]
            
            
   