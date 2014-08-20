def wordPigLatin(word):
        V = ['a', 'e', 'i', 'o', 'u']
        C = ['th','tr','br','cr','st','str','chr','sh','pr','wh','dr','ch', 'sc', 'scr', 'bl', 'bb', 'bbb', 'bbbb']      
        
        if word[0] in V:
                pltrans = word + "way"
        else:
                if word [:4] in C:
                        pltrans = word[4:] + "a" + word[:4] + "ay"
                elif word[:3] in C:
                        pltrans = word[3:] + "a" +word[:3] +"ay"                
                elif word[:2] in C:
                        pltrans = word[2:] + "a" + word[:2] + "ay"
                else: pltrans = word[1:] + "a" + word[0] + "ay" 
        return pltrans
     
def toPigLatin(s):
       
        words = s.split()
        pl_list = []
        pl_sentence = ""
        for word in words:
                pl_list.append(wordPigLatin(word))
     
        for pltrans in pl_list:
                pl_sentence = pl_sentence + pltrans + " "
        return pl_sentence    
 
 
def wordEnglish(word):
        Cr = ['ht', 'rt', 'rb', 'ts', 'rts', 'rhc', 'hs', 'rp', 'hw', 'rd', 'cs', 'mhs', 'lb', 'bb', 'bbb', 'bbbb'] 
       
        if word[:len(word) - 4:-1] == 'yaw':
                engtrans = word[:len(word) - 3]
        else:
                step1 = word[:len(word) - 5]
                step3 = word[:len(word) - 4]
                step4 = word[:len(word) - 6]
                step7 = word[:len(word) - 7]
                step8 = word[-3:-7:-1]
                step2 = word[-3:-5:-1]
                step5 = word[-3:-6:-1]
                step6 = word[-3]
                if word[-3:-7:-1] in Cr:
                        engtrans = step8[::-1] + step7
                elif word[-3:-6:-1] in Cr:
                        engtrans = step5[::-1] + step4 
                elif word[-3:-5:-1] in Cr:
                        engtrans = step2[::-1] + step1
                else: engtrans = step6 + step3 
        
                                                   
        return engtrans 

                        
def toEnglish(s):
        
        words = s.split()
        eng_list = []
        eng_sentence = ""
        for word in words:
                eng_list.append(wordEnglish(word))
             
        for engtrans in eng_list:
                eng_sentence = eng_sentence + engtrans + " "
        return eng_sentence                          
       



        
     
        

       
 

    
            
       
       
            
    
                
            