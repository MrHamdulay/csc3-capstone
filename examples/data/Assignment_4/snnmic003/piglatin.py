# Michael Sanne
# 2014/03/31
# Question 3 Pig Latin

def toPigLatin (s):
        sentence = ""
        space = s.find (" ")
        repeat = s.count(" ")
        for i in range (repeat+1):
                if i == repeat:
                        word = s
                else:
                        word = s[0:space]
                vowel = -1
                for i in range (len(word)):
                        if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
                                vowel = i
                                break
                if (vowel == 0):
                        word += "way"
                elif (vowel == -1):
                        word = "a" + word + "ay"
                else:
                        word = word[vowel:] + "a" + word[0:vowel] + "ay"
                sentence += word + " "
                s = s[space+1:]
                space = s.find (" ")
        return (sentence)
        

def toEnglish(s):
        sentence = ""
        space = s.find(" ")
        repeat = s.count (" ")
        for i in range (repeat+1):
                if i == repeat:
                        word = s[0:-2]
                else:
                        word = s[0:space-2]
                        
                for i in range (len(word) -1, -1, -1):
                        if (word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' or word[i] == 'w'):
                                vowel = i       
                                break
                word = word[vowel+1:] + word[0:vowel]
                
                sentence += word + " "
                s = s[space+1:]         
                space = s.find (" ")
        return (sentence)        