def toPigLatin (s):
    s=str(s)
    sm=""
    for i in s.split():
        if i[0:1] in "aeiou":
            i+="way "
            sm+=i
            
        elif i[0:1] not in "aeiou":
            sm1=""
            for j in i:
                if j not in "aeiou":
                    x=j
                    sm1+=x
                elif j in "aeiou":
                    break
                sm2=""
                for k in i:
                    if k not in sm1:
                        y=k
                        sm2+=y
                    else :break
            wrd=i[len(sm1):]+"a"+sm1+"ay"+" "
            sm+=wrd
        #sm=sm[0:]
    #print(sm)
    return sm
        
def toEnglish (s):
    s=str(s)
    sm=""
    for i in s.split():
        #print(i)
        if i[-3::]=="way":
            i=i[0:(len(i)-3):]
            sm+=i+" "
        elif i[-2::]=="ay":
            q=i[0:(len(i)-2):]
            sm1=""
            for x in q:
                if x!="a":
                    y=x
                    sm1+=y
                else:break
                sm2=""
                for f in q:
                    if f in "a":
                        continue
                    else: 
                        t=f
                        sm2=t
                    word=sm2+sm1
            sm+=word+" "
        #print(sm)
        
    return sm
    
            
                    
    
                    
                
            
    