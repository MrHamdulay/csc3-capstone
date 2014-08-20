#Aiden Walton
# WLTAID001
#PigLatin translator

def toPigLatin(s):
    s1=s.split(" ")
    s_new=""
    for s in s1:
        if s[0]=="a" or s[0]=="e" or s[0]=="i" or s[0]=="o" or s[0]=="u":
            s_new+=s+"way"+" "
        else:
            pos=0
            cons_s=""            
            for i in s:
                if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                    break            
                else:
                    cons_s+=i
                    pos+=1
            s_new+=s[pos:]+"a"+cons_s+"ay"+" "
    return s_new

def toEnglish(s):
    s1=s.split(" ")
    s_new=""
    for s in s1:
        n=len(s)
        if s[n-3:n]=="way":
            s_new+=s[:n-3]+" "
        elif s[n-2:]=="ay":
            s_orig=s[:n-2]
            s_rev=s_orig[::-1]
            f=s_rev.find("a")
            s_cons=s_rev[:f]
            s_cons=s_cons[::-1]
            s_orig1=s_rev[f+1:]
            s_new+=s_cons+s_orig1[::-1]+" "
    return s_new

        
                 

    

                
            