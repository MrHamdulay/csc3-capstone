
def toPigLatin(phrase):
    final=""
    phrase_split=phrase.split()
    for i in phrase_split:
        count=0
        word=0
        num=0
        for j in "aeiou":
            if i[0]==j:
                word=i+"way"
                final+=(word+" ")
                break
            elif i[0]!=j and num<5:
                num+=1
                if num>=5:
                    cons=-1
                    new=0
                    for c in i:
                        cons+=1
                        new+=1
                        fin=0
                        for m in "aeiou":
                            if count==1:
                                break
                            elif m!=c:
                                fin+=1
                                if i[len(i)-1]!="u" and new==len(i) and fin==5:
                                    final+="a"+i+"ay"+" "
                                    break                               
                                else: continue
                            elif m==c:
                                final+=((i[cons:len(i)]+"a"+i[0:cons]+"ay")+" ")
                                count+=1
                                break
    return final
 
def toEnglish(phrase):
    final=""
    inbetween=""
    phrase_split=phrase.split()
    for i in phrase_split:
        count=0
        word=0
        num=0
        if i[len(i)-3:len(i)]=="way":
                word=i[0:(len(i)-3)]
                final+=(word+" ")
                continue
        else:
            inbetween=""
            word=i[0:len(i)-2]
            sam=word[::-1]
            for c in "a":
                for j in sam:
                    if count==1:
                        break
                    if c!=j:
                        inbetween+=j
                        num+=1
                        continue
                    else:
                        count+=1
                        steve=inbetween[::-1]
                        sam=sam[num+1:len(sam)]
                        new=steve+sam[::-1]
                        final+=(new+" ")
                        break
    return final