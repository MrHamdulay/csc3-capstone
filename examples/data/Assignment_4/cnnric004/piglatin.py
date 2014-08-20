def toPigLatin(s):
        
        
        pigSentence = ""
        seqOfConsonants = ""
        seqOfConsonantsOne = ""
        firstWord = 0
           
        for i in s.split(" "):
                
                if((i[:1].lower()=="a")or(i[:1].lower()=="e")or(i[:1].lower()=="i")or(i[:1].lower()=="o")or(i[:1].lower()=="u")):
                        if(firstWord == 0):
                                pigSentence += i + "way"
                        else:
                                pigSentence += " " + i + "way"
                else:
                        for k in range(1,len(i)):
                                seqOfConsonantsOne =""
                                if((i[k:k+1].lower()!="a")and(i[k:k+1].lower()!="e")and(i[k:k+1].lower()!="i")and(i[k:k+1].lower()!="o")and(i[k:k+1].lower()!="u")):
                                        seqOfConsonants = i[:k+1]
                                elif((i[k:k+1].lower()=="a")or(i[k:k+1].lower()=="e")or(i[k:k+1].lower()=="i")or(i[k:k+1].lower()=="o")or(i[k:k+1].lower()=="u")):
                                        if(k==1):
                                                seqOfConsonantsOne = i[:k]
                                        break
                                
                        if(seqOfConsonantsOne!=""):
                                if(firstWord == 0):
                                        pigSentence += i[k:] + "a" + seqOfConsonantsOne + "ay"
                                else:
                                        pigSentence += " " + i[k:] + "a" + seqOfConsonantsOne + "ay"
                        else:
                                if(firstWord == 0):
                                        pigSentence += i[k:] + "a" + seqOfConsonants + "ay"
                                else:
                                        pigSentence += " " + i[k:] + "a" + seqOfConsonants + "ay"
                                
                firstWord=1
                        
        return pigSentence
                                        
                                                                        
#PigLatin Sentence =       Iway amway omafray eathay outhasay ideasay eenascray                                                                        
def toEnglish(s):
        
        englishSentence=""
        wordAfterConsonants=""
        consonants=""
        posOfA = 0
        firstWord = 0
        
        for i in s.split(" "):
                wordAfterA=i
                if(i.find("way") != -1):
                        if(firstWord == 0):
                                englishSentence += i[:i.find("way")]
                        else:
                                englishSentence += " " + i[:i.find("way")]
                                
                                
                else:
                        for k in range(len(i)):
                                wordWithoutay = i[:i.find("ay")]
                                if(wordWithoutay.find("a")!=-1):
                                        wordAfterA = wordWithoutay[wordWithoutay.find("a")+1:]
                                        posOfA = wordWithoutay.find("a")
                                else:
                                        consonants = wordAfterA
                                        break
                                
                        wordAfterConsonants = i[:posOfA]
                        if(firstWord == 0):
                                englishSentence += wordAfterA + i[:i.find("a")]
                        else:
                                englishSentence += " " + wordAfterA + i[:i.find("a")]
                        
                firstWord = 1
        return englishSentence
                        