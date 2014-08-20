
def toPigLatin(s):
    words=s.split(" ")
    new_s=''
    for i in words:
        if i[0]!='a' and i[0]!='e' and i[0]!='i' and i[0]!='o'and i[0]!='u'and len(i)==1:
            new_word=('a'+i+'ay')
            new_s=new_s+new_word+' '        
        elif i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o'or i[0]=='u':
            new_word=(i + 'way')
            new_s=new_s + new_word+' '
        
            
        elif len(i)==1:
            break             
            
        elif i[1]=='a' or i[1]=='e' or i[1]=='i' or i[1]=='o' or i[1]=='u':
            new_word=(i[1:] +'a'+i[0]+'ay')
            new_s=new_s + new_word+' '
        elif i[1]!='a' and i[1]!='e' and i[1]!='i' and i[1]!='o'and i[1]!='u'and len(i)==2:
            new_word=('a'+i+'ay')
            new_s=new_s+new_word+' '            
        
        elif len(i)==2:
            break              
        
        elif i[2]=='a' or i[2]=='e' or i[2]=='i' or i[2]=='o' or i[2]=='u':
            new_word=(i[2:] +'a'+i[0]+i[1]+'ay')
            new_s=new_s + new_word+' '
        elif i[2]!='a' and i[2]!='e' and i[2]!='i' and i[2]!='o'and i[2]!='u'and len(i)==3:
            new_word=('a'+i+'ay')
            new_s=new_s+new_word+' '            
        
        elif len(i)==3:
            break                   

        elif i[3]=='a' or i[3]=='e' or i[3]=='i' or i[3]=='o' or i[3]=='u':
            new_word=(i[3:] +'a'+i[0]+i[1]+i[2]+'ay')
            new_s=new_s + new_word+' ' 
        elif len(i)==4:
            break
        else:
            new_word=('a'+i+'ay')
            new_s=new_s+new_word+' '            
    return new_s       

def toEnglish (s):
    words=s.split(" ") 
    new_s=''
    for i in words:
        if i[-1:-4:-1]=='yaw':
            x=(len(i)-3)
            new_word=(i[0:x:1])
            new_s=new_s+new_word+' '
        elif i[-4]=='a' or i[-4]=='e' or i[-4]=='i' or i[-4]=='o' or i[-4]=='u':
            y=len(i)-2
            new_word=(i[0:y:1])
            z=len(new_word)-2
            new_word=(new_word[-1]+new_word[0:z:1])
            new_s=new_s+new_word+' '
        else:       
            y=len(i)-2
            new_word=(i[0:y:1])
            z=len(new_word)-3
            new_word=(new_word[-2]+new_word[-1]+new_word[0:z:1])
            new_s=new_s+new_word+' '
    return new_s       
                