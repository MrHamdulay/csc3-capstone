# Michaela Heale
#Assignment 4 Question 3

def toPigLatin(s):
    sentence = []
    sentence = s.split(' ')
    sln = len(sentence)
    newpig = ""
    for z in range(0,sln,1):
        pig = ""
        word = sentence[z].lower()
        first = word[0]
        #deals with vowel firsts
        if (first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u'):
            pig = word+"way"
            newpig += pig+ " "
        #deals with consonant firsts
        else:
            wln = len(word)
            pos = 0
            p = 1
            while pos == 0:
            #finds the posiition of the last in the row of consonants at the beginning
                char = word[p]
                if(char=='a' or char=='e' or  char=='i' or char=='o' or char=='u'):
                    pos=p
                else:
                    p+=1
                        
            cons = word[0:pos]
            vowl = word[pos:wln]
            pig = vowl+"a"+cons+"ay"
            newpig += pig+ " "
    return newpig

def toEnglish(s):
    sentence = []
    sentence = s.split(' ')
    sln = len(sentence)
    neweng = ""    
    for z in range(0,sln,1):
        eng = ""
        word = sentence[z].lower()
        wln = len(word)
        end = word[wln-3:wln]
        if (end == "way"):
        #deals with converting back to vowel firsts
            eng = word[0:wln-3]
            neweng += eng+" "
        else:
        #deals with converting back to consonant firsts
            wordd = word[0:(wln-2)]
            pos = len(wordd)
            p = len(wordd)-1
            while pos == len(wordd):
                char = wordd[p]
                if (char == 'a'):
                    pos = p
                else:
                    p -= 1
            cons = wordd[pos+1:wln]
            vowl = wordd[0:pos]
            eng = cons+""+vowl
            neweng += eng + " "
    return neweng

    
