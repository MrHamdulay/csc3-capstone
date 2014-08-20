"""assignment4
question3
THNSIK001"""

def toPigLatin(s):
    pigl = str(s)
    cons1=False
    countk=0
    vowels = "aeiou"
    for i in vowels:
        if(s[0]==i):
            s=s+"way"
        for k in s:
            if not(k==i):
                cons1=True
                if k==0:
                    pigl+="a"
                pigl = pigl[(countk+1):-1]+pigl[countk]
            countk+=1
    if(cons1):
        pigl+="ay"
        
    return pigl

def toEnglish(s):
    eng = str(s)
    if(s[-3:-2]=="way"):
        eng = eng[0:-4:1]
    else:
        eng=s[0:-2:1]
        for i in eng[::-1]:
            if not i=="a":
                eng=eng[i]+eng[0:i-1]
            else: break
        return eng[0:-2:1]