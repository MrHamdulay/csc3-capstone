def toPigLatin(x):
    

    words = x.split(" ")
    pos = 0
    cons = ""
    numcons = 0
    s = ""

    for i in words:
        if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u':
        
        
            words[pos] = words[pos] + "way"

            pos+=1
    
        else:
            for j in range (len(i)):
                if i[j] == 'a' or i[j] == 'e' or i[j] == 'i' or i[j] == 'o' or i[j] == 'u':
                    break
                else:
                    cons += i[j]
                
                    numcons+=1
            words[pos] = words[pos][numcons:] + "a" + cons + "ay"
            numcons = 0
            cons = ""
            pos+=1        
                
    for i in words:
        s += i + " "
    return s

def toEnglish(x):
        
        words = x.split(" ")
        back = -3
        reverse = ""
        backcnt = 2
        pos = 0
        s = ""
        w = 0
        for i in words:
        
            #if i[-2] + i[-1] == "ay" and i[-3]!= "w":
            

            if i.count("w")==0:
                
                for j in range (len(i)-2):
                    if i[back] == 'a':
                        break
                    else:
                
                    
                        reverse += i[back]
                        back -=1
                        backcnt+=1
          
                
                    words[pos] = reverse[::-1] + i[:len(i) - backcnt-1]
           


            
            else:
                words[pos] = i[:len(i)-3]


            pos+=1
            reverse = ""
            back = -3
            backcnt = 2
            w = 0

        for i in words:
            s += i + " "
        return s





    

