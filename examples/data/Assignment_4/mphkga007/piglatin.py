#convert english words to piglatin and back to  english from piglatin
#03/04/2014
#kkmphele

def toPigLatin (s):
    
    s_split=s.split() #spliting the string
    lis=[s_split] #make the string in a kind of a  list of words
    for i in range(len(lis)):  #counts how many words i have  in the string
        d=lis[i]    # d strings every word in the sentence
        for n in range(len(d)):# how many stringed  word i have
            e=d[n]             #assing e to every word in the sentence
            first_letter=e[0] #takesthe first letter at the beginning of every word 
            second_letter=e[1] #take the secnd letter at the beginning of every word
            vowels=["a","e","i","o","u"]
            consonants=["b","c","d","f","g","h","t","j","k","l","m","n","p","q","r","s","v","w","x","y","z"]
            for i in range(len(vowels)): #counts how many vowels i have
                
                v=vowels[i]  #assigns v to every vowels in the list of vowels(vowels)
                if v==first_letter: #checks whether the first letter of a string  is a vowel
                    pig="way"
                    new_word=e+pig
                    return new_word
                    
            for x in range(len(consonants)): #counts how many consonants are in list of consonants
                
                c=consonants[x]  #assign every consonant to c
                if c==first_letter: # checks if the first letter of every word in the striing is consonant or  no
                    for i in range(len(vowels)): 
                        v=vowels[i]
                        if v==second_letter :
                               siffix=e[0:1]
                               pyg="ay"
                               lefte=e[1:]
                               new_l=lefte+"a"+siffix+pyg
                               return new_l
                               #print(new_l,end=" ")
                    for s in range(len(consonants)):
                        b=consonants[s]
                        if b==second_letter:
                            suffix=e[0:2]
                            pyg="ay"
                            left=e[2:]
                            new=left+"a"+suffix+pyg
                            return new
                            #print(new,end=" ")
    #print(new_word,new_l,new)
                            
#toPigLatin("the quick black fox jumps over the lazy apple")

              
            
            
        
def toEnglish (s):
    s_split=s.split()
    lis=[s_split]
    for i in range(len(lis)):
        d=lis[i]
        for n in range(len(d)):
            letter=d[n]
            third=letter[-3]
            four=letter[-4]
            q=letter[-5]
            
            if third=="w":
                new_word=letter[:-3]
                return new_word
                #print(new_word,end=" ")
            if four=="a":
                a=letter[:-4]
                b=letter[-3]
                new=b+a
                return new
                #print(new,end=" " )
            if q=="a":
                z=letter[:-5]
                l=letter[-4:-2]
                few=l+z
                return few
                #print(few,end=" ")
        #return
            
           
                

         
    
    

    