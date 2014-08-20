#zikho godana
#03 april 2014
#module to translate sentences between English and a variant of Pig Latin

def toPigLatin(s):
    new=''
    word=s.split() #slpit the string into words only
    for i in word:
        if i[0]in'aeiou':
            new=new+i+'way'+' '
        else:
            index=0
            c=0
            for j in i:
                if j[c] not in 'aeiou': 
                    index+=1
                else:
                    break    
        
            new=new+i[index:]+'a'+i[0:index]+'ay'+' '
    return new

def toEnglish(s):
    new=''
    new1=''
    word=s.split()
    for i in word:
        if i[len(i)-3] in 'w':
            new=new+i[:len(i)-3]+' '
        else:
            new1=i[:len(i)-2]
            index=0
            #print(new1,new1[len(new1)-1])
            #for j in new1:
            print(new1[len(new1)-2])
            
            if new1[len(new1)-3]in 'a':
                new=new1[len(new1)-2:len(new1)]+new1[0:len(new1)-3]
            elif new1[len(new1)-2]in'a':
                new=new1[len(new1)-1:len(new1)]+new1[0:len(new1)-2]            
            elif new1[len(new1)-4]in 'a':
                new=new1[len(new1)-3:len(new1)]+new1[0:len(new1)-3]+' '
            #else:
                #break
        
            #print(new1,new)
                

    return new
            
            
#word=toEnglish('eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway ')
#print(word)