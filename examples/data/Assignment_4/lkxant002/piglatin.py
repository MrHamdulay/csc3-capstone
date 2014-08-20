def toPigLatin(s):
    ss=s.split()
    sfin=""
    for i in range(len(ss)):
        vowel=0
        if ss[i][0]=="a" or ss[i][0]=="e" or ss[i][0]=="i" or ss[i][0]=="o" or ss[i][0]=="u":
            ss[i]=ss[i]+"way"
        else:
            for l in ss[i]:
                if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
                    vowel=1
            if vowel==1:
                k=0
                j=0
                while not(j=="a" or j=="e" or j=="i" or j=="o" or j=="u"):
                    k=k+1
                    j=ss[i][k]
                ss[i]=ss[i][k:]+"a"+ss[i][:k]+"ay"                
            if vowel!=1:
                ss[i]="a"+ss[i]+"ay"
                    
        
        sfin=sfin+" "+ss[i]
    return(sfin[1:])

def toEnglish(s):
    ss=s.split()
    sfin=""
    for i in range(len(ss)):
        k=""
        if ss[i][-3]=="w":
            ss[i]=ss[i][:-3]
        else:
            ss[i]=ss[i][:-2]
            for j in range(len(ss[i])):
                if ss[i][-j-1]=="a":
                    k=j
                    break
            ss[i]=ss[i][-j:]+ss[i][:-j-1]
            
        sfin=sfin+" "+ss[i]
    return(sfin[1:])    

