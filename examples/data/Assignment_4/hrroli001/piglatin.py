# Question 3 - Assignment 4
# Oliver Harrison
# 01 April 2014

def toPigLatin(s):
    x=""
    for ch in (s).split():
        if ch[0:1]=="a" or ch[0:1]=="e" or ch[0:1]=="i" or ch[0:1]=="o" or ch[0:1]=="u":
            #print (ch+"way", end=" ")
            x = x + ch + "way" + " "
            #print(x, end="")
        else:
            cons=0
            for y in ch:
                if y!="a" and y!="e" and y!="i" and y!="o" and y!="u":
                    cons+=1
                else: 
                    break
            #print (ch[cons:], "a", ch[:cons], "ay", sep="", end=" ")
            x = x + ch[cons:] + "a" + ch[:cons] + "ay" + " "
            #print(x, end="")
            
    return x
                
                    
#print(toPigLatin("the quick black fox jumps over the lazy apple"))

def toEnglish(s):
    x=""
    for word in (s).split():
        if word[(len(word)-3):]=="way":
            x = x + word[:len(word)-3] + " "
        else:
            word=word[:len(word)-2]
            backwards=(word[::-1])
            #print(word)
            #print(backwards)
            count=0
            for i in backwards:
                if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":
                    count+=1
                else:
                    break
            x = x + word[len(word)-count:] + word[:len(word)-count-1] + " "
    return x
            
       
#print(toEnglish("eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway"))      
            
