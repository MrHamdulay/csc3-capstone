def toPigLatin(s):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U",'',' ')	 
    sentence = s
	     
    words =  sentence.split()
    new=[]	     
    for word in words:
        if word[0] in vowels:
            a = new.append(str(word + "way"))
        else:
            if len(word) > 1:
                if len(word) >=4 and word[0] not in vowels and word[1] not in vowels and word[2] not in vowels and word[3] not in vowels:
                    a = new.append(str( word[4:]+ "a" + word[0:4] + "ay"))
                elif len(word) >=3 and word[0] not in vowels and word[1] not in vowels and word[2] not in vowels:
                    a = new.append(str( word[3:]+ "a" + word[0:3] + "ay"))
                elif len(word) >=2 and word[0] not in vowels and word[1] not in vowels:
                    a = new.append(str( word[2:]+ "a" + word[0:2] + "ay"))                
                elif len(word) > 2 and word[0] not in vowels and word[1] in vowels:
                    a = new.append(str( word[1:]+ "a" + word[0] + "ay"))
                else:
                    a = new.append(str( word[1:]+ "a" + word[0] + "ay"))                
            else:
                a = new.append(str( word[1:]+ "a" + word[0] + "ay"))            
                       
            
                        
            
                        

    b = ' '.join(new)
    return(b)

def toEnglish(s):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    sentence = s
	     
    words =  sentence.split()
    new=[]	     
    for word in words:
        if word[::-1][:3] == "yaw":
            a = new.append(str(word.replace('way','')))
        elif word[-3:-2] not in vowels and word[-4:-3] in vowels:
            a = new.append(str(word[-3]+word[0:-4]))
        elif word[-3:-2] not in vowels and word[-4:-3] not in vowels and word[-5:-4] in vowels:
            a = new.append(str(word[-4:-2]+word[0:-5]))
        elif word[-3:-2] not in vowels and word[-4:-3] not in vowels and word[-5:-4] not in vowels and word[-6:-5] in vowels:
            a = new.append(str(word[-5:-2]+word[0:-6]))
        elif word[-3:-2] not in vowels and word[-4:-3] not in vowels and word[-5:-4] not in vowels and word[-6:-5] not in vowels and word[-7:-6]:
            a = new.append(str(word[-6:-2]+word[0:-7]))            
    

    b = ' '.join(new)
    return(b)