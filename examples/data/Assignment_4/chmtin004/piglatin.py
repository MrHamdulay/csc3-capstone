"""PIGLATIN.py module for Question3
Tinotenda Chemvura (CHMTIN004)
31 March 2014"""

def toPigLatin (s):
    """function to convert English to Pig Latin"""
    #s = input("Enter an English sentence:\n")
    #s = s.lower()
    #w = len(s.split())
    snew = ""
    for i in s.split():
        if i[0] in "aeiou":                                   #if i starts with a vowel, add "way" to it
            i+="way "
            snew+=i                                           #add the new i to the new sentence
        elif i[0] not in "aeiou" :
            i+="a"                                            # adding "a" to the word "i"
            cons = ""                                         #cons = the sequence of consonants 
            for j in i:
                if j not in "aeiou":                          #got through letter in i and if 
                    cons+=j                                   #they are consonants, add them to cons
                if j in "aeiou":           
                    break                                     #stop loop if j is a vowel
            i = i[len(cons)::] + cons + "ay "                 #new i starts frm where the cons ws cut off
            snew+=i
        snew2 = snew[:-1]
    #print(snew2) #testing module
    return snew2
    
        
#toPigLatin("please")        
#toPigLatin("the quick black fox jumps over the lazy apple")   #testing module

def toEnglish (s):
    """Function to convert Pig Latin to English"""
    #s = s.lower()
    snew3 = ""
    for i in s.split():
        if i[-3] == "w":                    #if the 3rd letter from last is "w"
            i = i[:-3]                      #remove the last 3 characters "way"
            snew3 = snew3 + i + " "         #add the new i to the sentence snew3
        elif i[-3] != "w":                  #if the 3rd letter from last is not "w"
            i = i[:-2]                      #remove last two "ay" characters
            cons = ""                       #variable to save my consonents
            for j in i[-1:0:-1]:            #going through the consonents from the last character...
                if j not in "aeiou":        
                    cons+= j                #save the consonents as a single string
                if j == "a":                #...until "a" is reached then stop the j loop
                    break
            
            count = len(cons) + 1           
            count = (count * -1)
            i = i[:count:]                  #remove the consonents and the character "a" (hence the +1 in count)
            cons = cons[::-1]               #reverse the order of consonents
            i = cons + i                    #add the cons to the beginning of the word i
            snew3 = snew3 + i + " "         #add i to the sentence and a space
        sn = snew3[:-1]                     # remove the last space in the sentence
    #print(sn)                              # command for testing the function
    return sn                               #return the new sentence
    
#toEnglish("elloaHay orldaWay")   #this is "please" in english
#toEnglish ("eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway")