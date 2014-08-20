#Question3 piglatin.py 
#Brandon Hall (HLLBRA005)
#4 April 2013

def toPigLatin(s):
    length = len((s.split(" ")))
    trans = ""
    for i in range (length):
        word = (s.split(" ")[i])
        #print (word)
                
        if (word[0:1] is 'a' or word[0:1] is 'e' or word[0:1] is 'i' or word[0:1] is 'o' or word[0:1] is 'u'):
            trans += word+"way "
        else:
            for j in range(len(word)):
                if (word[j:j+1] is 'a' or word[j:j+1] is 'e' or word[j:j+1] is 'i' or word[j:j+1] is 'o' or word[j:j+1] is 'u'):
                    x = j
                    break
            cons = word[0:x]
            
            trans += word[x:] + "a" +cons + "ay "
    return trans
        
        
def toEnglish(s):
    length = len((s.split(" ")))
    trans = ""
    word = s.split()
    
    for words in word:
        
       
        
        
        if words[-3:] == 'way':
            trans += words[0:(len(words)-3)]+" "
            
        elif words [-2:] == 'ay':
            trim = words[:-2]
            a = trim.rfind("a")
            beginning = trim[a+1:]
           # print(a)
          #  print (trim)
           #print(beginning)
            nWord = beginning+trim[0:a]
            newWord = nWord+" "
            
            #print(newWord)
            
            trans+=newWord
           
          
       
         
              
    return trans                       
          