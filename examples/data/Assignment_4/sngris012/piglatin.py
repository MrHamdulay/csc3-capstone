def toPigLatin(s):
    s=s.split(" ")
    wordd=""
    k=0
    for i in s:
        tempo=i[0]
        t=1
        if(i[0] in {'a','e','i','o','u'}):
            wordd+=i+"way"
        else:
            
            while((t<=len(i)-1) and (i[t] not in {'a','e','i','o','u'})):
                tempo+=i[t]
                t+=1
            if(t<=len(i)-1):
                wordd+=i[t:len(i)]+"a"+tempo+"ay"
            else:
                wordd+="a"+tempo+"ay"
        if(k!=len(s)-1):
            wordd+=" "
        k+=1
    return wordd

def toEnglish(s):
    s=s.split(" ")
    wordd=""
    k=0
    for i in s:
        t=len(i)-3
        tempo=""
        c=0
        for j in i:
            if(j=='w'):
                wordd+=i[0:len(i)-3]
                c+=1
        if(c==0):
            while(i[t] not in {'a','e','i','o','u'}):
                tempo+=i[t]
                t-=1
            wordd+=tempo[::-1]+i[0:t]
        if(k!=len(s)-1):
            wordd+=" "
        k+=1
    return wordd       