def toPigLatin(s):
    x=s.split()
    p=""
    for i in x:
        if i[0] not in "AEIOUaeiou" :
            y=-1
            for j in i :
                if j not in "AEIOUaeiou" :
                    y+=1
                if j in "AEIOUaeiou" : 
                    break
            p+=i[y+1:len(s)+1]+"a"+i[0:y+1]+"ay"+" "        
        elif i[0] in "AEIOUaeiou" :
            p+=i+"way"+" "
        
    return p

def toEnglish(s):
    x=s.split()
    p=""
    for i in x :
        if "way" in i:
            p+=i[0:i.find("way")]+" "
        elif i.count("a")>=2 :
            i=i[0:len(i)-2]
            y=i[i.rfind("a")+1:len(i)]
            p+=y+i[0:i.rfind("a")]+" "
        elif i.count("a")==2 :
            consonant=i[i.find("a")+1:i.find("ay")]
            p+=consonant+i[0:i.find("a")]+" "
    
    return p 