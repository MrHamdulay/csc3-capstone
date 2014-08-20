vowels = ["a","e","i","o","u"]

def toPigLatin(s):
    string=""
    words=s.split()
    for i in range(len(words)):
        if words[i][0].lower() in vowels:
            words[i]=words[i]+"way"
        else:
            mark=0
            while words[i][mark].lower() not in vowels:
                mark+=1
                if mark==len(words[i]):
                    break
            words[i]=words[i][mark:len(words[i])]+"a"+words[i][0:mark]+"ay"
        if i==0:
            string=string+words[i]
        else:
            string=string+" "+words[i]        
    return(string)
     
def toEnglish(s):
    string=""
    words=s.split()
    for i in range(len(words)):
        if words[i].endswith("way"):
            words[i]=words[i][0:len(words[i])-3]
        else:
                mark1=words[i][0:len(words[i])-3].rfind("a")  
                words[i]=words[i][mark1+1:len(words[i])-2]+words[i][0:mark1]
        if i==0:
                string=string+words[i]
        else:
            string=string+" "+words[i]
    return(string)