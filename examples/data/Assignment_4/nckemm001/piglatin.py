# Emmalene Naicker
# Assignment 4         
# Question3

#Translating english to piglatin
def toPigLatin(s):
    green='w'
    blue=s.split(' ')
    purple=""
    
    for h in range(len(blue)):
        x=blue[h]
        if green in x:
            None
            
        else:
            aaa="AEIOU"
            bbb='aeiou'
            if x[0:1] in aaa or x[0:1] in bbb:
                x+='way'
                
            else:
                brown=0
                for i in range(len(x)):
                    if x[i] not in aaa and x[i] not in bbb:
                        brown+=1
                        continue
                    else: break
                    
                x=x[brown:]+'a'+x[0:brown]+'ay'
        purple+=x+' '
    return purple[:-1]

#Translating piglatin to english
def toEnglish(s):
    w=s.split(' ')
    purple=""
    for h in range(len(w)):
        yellow=w[h]
        
        if yellow[:-4:-1] =='yaw':
            yellow=yellow[:-3]
        else:
            yellow=yellow[:-2]
            x=0
            for i in yellow[::-1]:
                if i=='a':
                    yellow=yellow[len(yellow)-x:]+yellow[:len(yellow)-x-1]
                    break
                else:
                    x+=1
        purple+=yellow+' '
    return purple[:-1]
