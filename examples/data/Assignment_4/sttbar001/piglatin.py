"""English/piglatin converter
barak setton
31/03/2014"""
def toPigLatin (s):
    count1 =0
    count = 0
    i1 =0
    wordfull = ""
    word =""
    count2 = 0
    for i in str(s):
        if i == " ":
            count2 =0
            word = s[count1:count]
            count1 = count
            
            word =word.replace(" ","")
            ind = "aeiou".find(word[0:1])
            if ind != -1:
                wordfull =wordfull+" "+word+"way"
            else:
                le = len(word)
                for i in range(le):
                    ind = "aeiou".find(word[i:i+1])
                    
                    if ind != -1:
                        wordbeg = word[0:i]
                        word = word[i:] +"a"+wordbeg+"ay"
                        wordfull = wordfull+" "+word
                        break
                    else:
                        count2 += 1
                    
                if count2 == le:
                    
                    word = "a"+word+"ay"

                    wordfull = wordfull+" "+word                 
                
                        
        count += 1
    word1 = s[count1:]
    word = s[count1+1:]
    word =word.replace(" ","")
    ind = "aeiou".find(word[0:1])
    if ind != -1:
        wordfull = wordfull +" "+word+"way"
    else:
        le = len(word)
        count2 = 0
        for i in range(le):
            ind = "aeiou".find(word[i:i+1])
            if ind != -1:
                wordbeg = word[0:i]
                word = word[i:] +"a"+ wordbeg+"ay"
                wordfull = wordfull+" "+word
                break
            else:
                count2 += 1
        if count2 == le:
            word1 =word1.replace(" ","")
            word = "a"+word1+"ay"
            wordfull = wordfull+" "+word            
                       
    wordfull = wordfull[1:]
    return(wordfull)


def toEnglish(s):
    length = len(s)
    word = ""
    full=""
    count =0
    for i in range(length-1):
        if s[i:i+1]==" ":
            word = s[count:i]
            
            word = word.replace(" ","")
           
            if word[-3:]=="way":
                word = word[0:-3]+" "
            else:
                word=word[:-2]
                length = len(word)
                num =0
                for k in range(length):
                    let = word[k:k+1]
                    if let =="a":
                        num = k
                word = word[num+1:]+word[0:num]+" "
            full = full + word
            
            count=i
    word = s[count:]
    word =word.replace(" ","")

    if word[-3:]=="way":
        word = word[0:-3]+" "
    else:
        word=word[-3:-2]+word[0:-4]+" "           
    full = full + word        
        
        
                
    if word == "":
        word=s
        if word[-3:]=="way":
            full =word[0:-3]
        else:
            full=word[-3:-2]+word[0:-4]
           
    full =full[:-1]
    return(full)
