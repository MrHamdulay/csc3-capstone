
"""Jacob Ntesang
A program that converts two languages ,namely English and PigLaatin viec versa
04/04/2014"""


def toPigLatin(s):

    
    s=s.split()
    #print(s)
    pig=""
    
    for word in s:
        #print(word)
        
        
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            pig+=(word+"way"+" ")
            #print(pig,end=" ")
        
        else:
            cont=0
            for k in word:
                if k not in "aeiou":
                    cont+=1
                    
                
                else :
                    break
                    
            pig+=(str(word[cont:])+"a"+word[:cont]+"ay"+" ") #eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway
                
        
    return (pig)


def toEnglish(s):
    #Converts from PigLatins to normal English
    

    s=s.split()
    #print(s)
    pig=""
    
    
    for word in s:
        #print(word)
        cont=0
        if word[:-4:-1]=="yaw":
            pig+=word[:len(word)-3]+" "
            
            #print(pig)
            
        else:
            cont=0
            reserve=""
            value=word[-3::-1]
            #print(word)
            for k in value:
                    if k!="a":
                        cont+=1
                        
                        
                    
                    else:
                        break
            #print(cont)
            
            pig+=word[len(word)-cont-2:-2]+word[:len(word)-cont-3]+" "
    return (pig)
             

        
        
        
    
                 
            
        
        
    
        
        

        
    