def toPigLatin(text):
    text=text.split(" ")
    word=""
    p=0
    for i in text:
        variable=i[0]
        x=1
        if(i[0] in {'a','e','i','o','u'}):
            word+=i+"way"
        else:
            while((x<=len(i)-1) and (i[x] not in {'a','e','i','o','u'})):
                variable+=i[x]
                x+=1
            if(x<=len(i)-1):
                word+=i[x:len(i)]+"a"+variable+"ay"
            else:
                word+="a"+variable+"ay"
        if(p!=len(text)-1):
            word+=" "
        p+=1
    return word

def toEnglish(text):
    text=text.split(" ")
    word=""
    p=0
    for i in text:
        x=len(i)-3
        variable=""
        f=0
        for j in i:
            if(j=='w'):
                word+=i[0:len(i)-3]
                f+=1
        if(f==0):
            while(i[x] not in {'a','e','i','o','u'}):
                variable+=i[x]
                x-=1
            word+=variable[::-1]+i[0:x]
        if(p!=len(text)-1):
            word+=" "
        p+=1
    return word       