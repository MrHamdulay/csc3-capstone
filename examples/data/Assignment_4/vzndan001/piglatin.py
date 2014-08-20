def toPigLatin(s):
    VOWELS= ("a","e","i","o","u")
    finalsentence=""
    words = s.split()  # splits the typed sentence into separate words 
    for s in words:
        pl=""
        finalword = ""
        f = s[0] #checking the first letter
        #checking if a word starts with a vowel and adding "way"
        if f in VOWELS:
            finalsentence+=( s + "way"+" ")
            continue
        i=0
        for c in s: # if not a vowel, checking the for the first vowel index
            i+=1
            if c not in VOWELS:
                pl+=c
            else:
                break
        pl="a"+pl+"ay"
        if len(s) != 1:
            finalword = s[i-1:]+pl
        else:
            finalword = pl
        finalsentence+= finalword+" "
    finalsentence = finalsentence[:len(finalsentence)-1]    
    return finalsentence
        
  
     
def toEnglish(s):
    
    finalsentence =""
    words=s.split() # splits sentence into words
    VOWELS= ("a","e","i","o","u")
    for s in words:
        if (s[::-1])[:3] == "yaw":
            finalsentence+=s[:len(s)-3]+" "
            continue
        finalword = ""
        temp = ""
        
        temp = s[:len(s)-2]
        i=0
        for c in temp[::-1]:
            i+=1
            if c == "a":
                a = len(temp)-i
                break
        finalword = temp[:a]
        finalword = temp[a+1:]+finalword
        finalsentence+=finalword+" "
    finalsentence = finalsentence[:len(finalsentence)-1]
    return finalsentence
            
        
        
        
        
        
        
        #checking the first letter
        #checking if a word starts with a vowel and adding "way"
        
                  
    
        
    #else:
        #new_word=word[:lenword-2:] # this cuts off the last two letters ie "ay"
        #new_word= word[first english letter::]+word[:first english letter:]   # i need to figure how to determine which letters at the end go to the front 
        #sentence=sentence+new_word #adding every word to a string

    
