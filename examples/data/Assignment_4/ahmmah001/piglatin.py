def toPigLatin(s):
    string=""
    string2=""
    string3=""
    #choice=input("(E)nglish or (P)ig Latin?\n")
    #if choice=="E":
        #sent=input("Enter an english sentence:\n")
        
    s=s.split(" ")
    for i in (s):
        for j in i[0]:
            if j in "aeiou":
                string=string+i+"way"+" "
                
            else:
                for j in i:
                    if j not in "aeiou":
                        string2=string2+j
                    else:
                        break
                x=len(string2)
                string3=string3+i[x:]
                string=string+string3+"a"+string2+"ay"+" "
                string2=""
                string3=""
                
    return(string)
                    
def toEnglish(s): 
    string=""
    string2=""
    string3=""    
    #if choice=="P":
        #sent=input("Enter a Pig Latin sentence:\n")
    s=s.split(" ")
    for i in (s):
        if "w" in (i):
            length=len(i)-3
            rem=(i[0:length])
            string=string+rem+" "
        else:
            length=len(i)-2
            part1=(i[0:length])
            part1=(part1[-1::-1])
            for j in part1:
                if j != "a":
                    string2=string2+j
                else:
                    break
            string2=string2[-1::-1]
            long=len(string2)
            part1=(part1[-1:long:-1])
            string=string+string2+part1+" "
            string2=""
            part1=""
                                                            
    return(string)


    