def toPigLatin(s):
    s=s.split()
    PL_s=""
    for i in range(0,len(s)):
        word=s[i]
        if word[0] in "aeiou":
            word+="way"
        else:
            consonants=""
            con_count=0
            for j in range(0,len(word)):
                if word[j] not in "aeiou":
                    consonants+=word[j]
                    con_count+=1
                else:
                    break
            word= word[con_count: ]+"a"+consonants +"ay"
        PL_s+=word+" "
    return(PL_s[0:-1])
    
def toEnglish(s):
    s=s.split()
    E_s=""
    for i in range(0,len(s)):
        word=s[i]
        if "w" in word:
            word=word[0:-3]
        else:
            consonants=""
            con_count=0
            word=word[0:-2]
            for j in range(-1,-len(word),-1):
                if word[j] not in "aeiou":
                    consonants=word[j]+consonants
                    con_count+=1
                else:
                    break
            word=consonants+word[0:len(word)-con_count-1]
        E_s+=word+" "
    return(E_s[0:-1])

#    choice=input("(E)nglish or (P)ig Latin? \n")
 #   if choice=="E":
  #      s=input("Enter an English sentence: \n")
   #    print(toPigLatin(s))
    #elif choice=="P":
    #    s=input("Enter a Pig Latin sentence:\n")
     #   print("English")
      #  print(toEnglish(s))
    
#translate()