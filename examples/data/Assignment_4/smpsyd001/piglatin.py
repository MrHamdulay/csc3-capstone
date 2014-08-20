def toPigLatin(s):
    new=''
    for i in s.split(' '):
        f=i[:1]
        #print(f)
        if f=='a' or f=='e' or f=='i' or f=='o' or f=='u':
            new+=i+'way'+' '
            continue
        else:
            u=-1
            for j in i:
                u+=1
                if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
                    new+=i[u:]+'a'+i[:u]+'ay'+' '
                    break
                #new code
                elif u==len(i)-1:
                    new+='a'+i+'ay'+' '
                    
    return new
                    
            
def toEnglish(s):
    l=len(s)
    newstring=''
    for i in s.split(" "):
        if i[-2:]=='ay'and i[-3:]!='way':
            new=i[:len(i)-2]
            #print(new)
            u=0
            for j in new[-1:-len(new)-1:-1]:
                #print(j)
                u-=1
                if j=='a':
                    #print(u)
                    w=len(new)+u
                    newstring+=new[u+1:]+new[0:w]+' '
                    break
                
                    
        else:
            newstring+=i[:len(i)-3]+' '
    return newstring
                    