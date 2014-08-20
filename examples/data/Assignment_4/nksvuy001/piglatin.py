#piglatin.py
#vuyolwethu nkosi
#29 march 2014


def toPigL_initial(o):
#Convert to Pig Latin

    initial=len(o)
    word=o[0]
    vowel="aeiouAEIOU"
    
    if word in vowel:
        PigL_first=o+"way"
        return PigL_first
    
    else:
        v=0
    for run in o:
        if run in vowel:
            break
        v+=1
        u= v-1
        o_1=o[v:] # letters after the first consonants
        o_2=o[0:v] # first letter consonants
        PigL_second=o_1+'a'+o_2+'ay'
        return(PigL_second)


def toPigLatin(s):
#Separates words then converts the word to Pig Latin and then remakes the sentence

    s=s+" "
    o_second=""
    o =""
    
    for run in s:
        if run!=" ":
            o=o+run
    
        elif run==" ":
            PigL=toPigL_inital(o)+" "
            o_second=o_second+PigL
            o=""
        string_len=len(o_second)-1
        o_third=o_second[:string_len]
        return(o_third)
    
    
def toPigL_second(o):
    
    initial=len(o)
    v =initial-3
    u =o[v:]
    y =initial-2
    l =o[y:]
    vowel="aeiouAEIOU"
    
    if u == "way":
        anglais=o[:v]
        return(anglais)
    
    elif l=="ay":
        o_last=o[:y]
        o_lastlast=o_last[::-1]
        w=0
        e=len(o_lastlast)
    
    
    for run2 in o_lastlast:
        if run2 in vowel:
            break
        w+=1
    cnstnt=o_lastlast[:w]
    t=e-w-1
    cnstnt_lastlast=cnstnt[::-1]
    RoL=o_last[:t]
    isingisi=cnstnt_lastlast+RoL
    return(isingisi)


def  toEnglish(s):
#Separating words then converts the sentence to English then remakes sentence

    s=s+" "
    o_second=""
    o=""
    
    for run in s:
        if run!=" ":
            o=o+run
        elif run==" ":
            PigL=toPigL_second(o)+" "
            o_second=o_second+PigL
            o=""
        len_str=len(o_second)-1
        o_third=o_second[:len_str]
        return(o_third)
    

                

 