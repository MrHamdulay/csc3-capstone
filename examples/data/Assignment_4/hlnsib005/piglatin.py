def toPigLatin(s):
#sentence= "the quick black fox jumps over the lazy apple"
    s= s+ " "
    newsentence=""
    icount=0
    vowelword=""
    jcount=-1
    spacesentence=s
    spacecount=0
    spacefind=0
    while spacefind!= -1:
        spacefind= str.find(spacesentence," ")
        spacecount=spacecount+1
        spacesentence= spacesentence[spacefind+1:]
   
    while icount<(spacecount-1):
        position=(str.find(s, " "))
        icount=icount+1
        word= s[:position]
    
        if word[0] in "aeiou":
            newsentence=newsentence+ " "+ (word+"way")
        else:
            for j in word:          #QUICK   Q
                jcount=jcount+1     #0
                if j in "aeiou":   #no for Q   u therefore jcount= 1
                    vowelword= word[jcount:] + "a"+ word[:jcount] + "ay"  
                    newsentence= newsentence+ " " +vowelword
                    break
                else:
                    #print(j)
                    word=word[::-1]
                    vowelword= "a"+ word[jcount:]+ word[:jcount] + "ay"  
                    #print(vowelword)
                    newsentence= newsentence+ " " +vowelword
                    #print(newsentence)  
                    break                    
        s= s[position+1:]
    #print(sentence)
        jcount=-1
    return (newsentence[1:])

def toEnglish(s): 
    s= s+ " "
    newsentence=""
    draftsentence=""
    icount=0
    vowelword=""
    jcount=-1
    spacesentence=s
    spacecount=0
    spacefind=0
    n=""
    for j in s:
        if j in "w":
            continue
        n=n+j
    s=n
    
    while spacefind!= -1:
            spacefind= str.find(spacesentence," ")
            spacecount=spacecount+1
            spacesentence= spacesentence[spacefind+1:]
    
    while icount<(spacecount):
            position=(str.find(s, " "))
            icount=icount+1
            word= s[:position]
            #print(word)        
            positionfind= str.find(word, "ay")
            if positionfind!=(-1):
                    word=word[:positionfind]
                    #print(word)
                    s= s[position+1:]
                    draftsentence=draftsentence+" " +word
    draft= draftsentence[1:] + " "
    #print(draft)
    #print(s)
    #print(spacecount)
    s=draft.split()
    #print(s)
    vowels= ("a","e","i","o","u")
    vowelsf= ("e","i","o","u")
    const= ""
    #if str.find(s,"a,e,0,
    # check if word ends with a consonant, if yes, then check if there is an a before it
    #delete the a
    #store consonants
    #newword= constonant + beginning of word
    #store in new sentence
    for j in s:
        if j.find("a")==-1:
            continue        
        if j.endswith(vowels)== True:
            continue
        if j.endswith(vowels) == False:
                newword=j[:-1]
               # print(newword)
                if newword.endswith(vowelsf) ==True:  
                    continue
                else:
                    if newword.endswith(vowelsf) ==False:                       #lazy
                        newword2= j 
                       # print(newword)
                        #print(newword2)   
                        while newword2.endswith("a") ==False:                  #eath                    # eath     htea    th     ea  #const= ht    newword=  ea
                            const= const+newword2[-1]  
                            #print(const)           
                            newword2= newword2[:-1] 
                            #print(newword2)   
                        const= const[::-1]
                        #print(const)
                        tempword= const+ newword2[:-1]
                        #print(tempword)
                        pos=s.index(j)
                        s.remove(j)
                        s.insert(pos,tempword)
                        const=""
                        
    new_s= ' '.join(s)                    #pos= str.find(newword2,"a") 
    return(new_s)    
            
        
        
    

    
