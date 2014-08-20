def toPigLatin(s):
    
    c = "" #What to convert 
    
    s=s+" x" #Empty string
    
    
    while s != "x": # WHile it's not the empty string run the convertion
        
        part = s[:s.find(" ")] #
        
        s = s[s.find(" ")+1:]
        
        #s = part+1
        
        t=part[0]
        
        if t[0]=="a" or t[0]=="e" or t[0]=="i" or t[0]=="o" or t[0]=="u":
                    part +="way"        
        #if (t=="a"):
            #part += "way"
            #return part
        #elif (t=="e"):
            #part += "way"
        #elif (t=="i"):
            #part += "way"
        #elif (t=="o"):
            #part += "way" 
        #elif (t=="u"):
            #part += "way"              
            
        else:
            
            x=50
            
            a=part.find("a")
            
            if a==-1:a=x
            
            e=part.find("e")
            
            if e==-1:e=x
            
            i=part.find("i")
            
            if i==-1:i=x
            
            o=part.find("o")
            
            if o==-1:o=x
            
            u=part.find("u")
            
            if u==-1:u=x
            
            q=min(a,e,i,o,u)
            if q==x:
                part = "a"+ part + "ay"
            else:
                part = part[q:]+"a"+part[:q]+"ay"
       
        c = c + " " + part
        
    c=c[1:]
        
    return c

def toEnglish(s):
    
    c =""    
    
    s=s+" x"
    
    while s != "x":
        
        part = s[:s.find(" ")]
        
        s = s[s.find(" ")+1:]
        
        #x=
        
        if part[(len(part)-3):]=="way":
            
            part=part[:(len(part)-3)]
            
        else:
           
            part=part[:(len(part)-2)]
            
            v=part.rfind("a") 
            #a=part.rfind("A")
            
            part=part[(v+1):]+part[:v]
            
        c =c + " " + part
        
    c = c[1:]
        
    return c