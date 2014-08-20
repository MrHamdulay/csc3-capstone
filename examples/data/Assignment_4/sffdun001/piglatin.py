def toPigLatin(s):
    sen=s.split()
    vowels=["a","e","i","o","u"]
    for i in range(len(sen)):
        check =False
        for f in range(len(sen[i])):
            if sen[i][f] in vowels:
                break
        else:
            sen[i]="a"+sen[i]+"ay"
            check=True
       
        if check==False:
        
            if ("aeiou".find(sen[i][0].lower())!=-1):
                sen[i]=sen[i]+"way"
            else:   
                pos=-1
                for j in range(len(sen[i])):

                    if "aeiou".find(sen[i][0].lower())==-1:
                        sen[i]=(sen[i][1:]+sen[i][0])
                    else: 
                        pos=j
                        sen[i]=sen[i][:j*-1]+"a"+sen[i][-1*j:]
                        sen[i]+="ay"
                        break
                
    re=''       
    for i in sen:
        re+=i+" "  
    return re

 
def toEnglish(s):
    senN=""
    sen=s.split()
    
    for i in sen:
        cnt=0
        word=0
        num=0
        
        if i[-3:]=="way":
                word=i[:-3]
                senN+=(word+" ")      
                
        else:
            a=""
            word=i[:-2]
            part=word[::-1]
            
            for c in "a":
                
                for h in part:
                    
                    if cnt==1:
                        break
                    
                    elif c!=h:
                        a+=h
                        num+=1
                        
                    else:
                        cnt+=1
                        part2=a[::-1]
                        part=part[num+1:len(part)]
                        new=part2+part[::-1]
                        senN+=(new+" ")
                        
    return senN 
#x=toPigLatin("black bb cat awee")
#print(x)