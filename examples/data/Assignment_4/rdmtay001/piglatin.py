
    
    
def toPigLatin(s):
    s=str(s)
    pig_latin_word=""
    #words=s.lower()
    piggy_oik_oik=""
    #testing_for_w=s.find('w')
    # if testing_for_w ==-1 (there is no w, thereforerun program):
    # else:????!!! 
    words=s
    words=words.split(" ")
    
    for x in words:
        
        first_letter=x[0:1]
        
        if first_letter in ("a","e","i","o","u"):
            pig_latin_word+=x+'way'+" "
            #print(pig_latin_word)
            
        else:
            consenent=first_letter
            length_of_word=len(x)
            word_to_use=x[1:]
            
            for y in range(2,length_of_word+1):
                next_letter=word_to_use[y-2:y-1]
                if next_letter in ("b","c","d","f","g","h",'j','k','l','m','n','p','q','r','s','t','v','x','y','z'):
                    consenent=consenent+next_letter
                                
                else: break                
            length_of_consenent=len(consenent)
            
            close_to_final_word=word_to_use[length_of_consenent-1:]
            
            pig_latin_word+=close_to_final_word+"a"+consenent+"ay"+" "
            
    return pig_latin_word         
                
    
def toEnglish(s):
    english=""
    string=str(s)
    s=string.split(" ")
    for wordies in s:
        length_of_s=len(wordies)
        last_three_letters=wordies[length_of_s-3:length_of_s]
        if last_three_letters=="way":
            english+=wordies[:length_of_s-3]+" "
        #return english
        else:
            word_cut_out_ay=wordies[:length_of_s-2]
            length_of_new_word=len(word_cut_out_ay)
        
            backwards_word=word_cut_out_ay[(length_of_new_word)::-1]
        
            word_to_use=backwards_word[1:]
            consenents=word_cut_out_ay[length_of_new_word-1:length_of_new_word]
        
            tayla_radmore=len(word_to_use)
            for x in range(1,tayla_radmore+1):
                letter=word_to_use[x-1:x]
                if letter in ("b","c","d","f","g","h",'j','k','l','m','n','p','q','r','s','t','v','x','y','z'):
                    consenents=consenents+letter
                
                else: break
            number_of_consenents=len(consenents)
        
            almost_final_word=word_to_use[number_of_consenents:]
        
            final_consenents=consenents[::-1]
            final_rest_of_word=almost_final_word[::-1]
            english+=final_consenents+final_rest_of_word+" "
        #return final_word
    #print(final_word)
    return english        
        