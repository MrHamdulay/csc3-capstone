#Assigment 4 Q3
#B.Player
#30/03/2014

def toPigLatin(s):
    st = s.split() 
    sen=""
    for i in range(len(st)):
        if st[i][0].lower() in "aeiou":
            st[i]+="way"
           
        else:
            st[i]+="a"
            while st[i][0].lower() not in "aeiou":
                st[i]=st[i][1:]+st[i][0:1]              
            st[i]+="ay"
            
    for i in st:
        sen = sen+i+" "
    return sen[:len(sen)-1]


def toEnglish(s):
    st = s.split() 
    sen=""
    for i in range(len(st)):
        if st[i][-3:]=="way": 
            st[i]=st[i][0:-3]
            
        else:
            st[i]=st[i][:-2] 
            pos=st[i].rfind('a')
            st[i]=st[i][pos+1:]+st[i][:pos]
                
    for i in st:
        sen = sen+i+" "
    return sen[:-1]    
                
#print(toEnglish("elloaHay orldaWay"))