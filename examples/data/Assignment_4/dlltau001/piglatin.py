
                                           #Splits sentence into seperate words and appends 'way' if it starts with a vowel
                            

def toPigLatin(s):
                        
        
        sentence = ''
        
        for i in s.split():
            
                if i[:1] not in ('aeiou' or 'AEIOU'): #Words beginning with a sentence
                        for j in list(i):
                                if j in ('aeiou' or 'AEIOU'):
                                        
                                        index = i.find(j)
                            #rint(i[0:index])
                            
                                        sentence = sentence + i[index::] + 'a' + i[0:index] + 'ay '
                            
                                        break
                                elif i.__len__() == 1:
                                        
                                        index = i.find(j)
                                        sentence = sentence + 'a' + i[0:index+1] + 'ay '
            
                elif i[:1] in ('aeiou' or 'AEIOU'):
                        sentence = sentence + (i + 'way ')                            
            
                                          
        sentence = sentence[:-1]               
        return sentence
        
                                       
                
                        