def toPigLatin(s):
   
   
    total=''
    for i in s.split():
        if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u":
            
            total  += i+"way "
        
        
        else:
            for j in i:
                if j in "aeiou":
                    pig = i.find(j)
                    total+= i[pig:]+"a"+ i  [0:pig]+"ay "
                    break
    return total

def toEnglish(s):
    total=''
    for i in s.split():
        if i[-3:]=="way":
            eng=i[0:-3]
        else:
            pig  =  i[0:-2]
           
            if pig[-2:] =="bl" or pig [-2:]=="th":
                eng  =  pig[-2:]  + pig [0:-2]
                eng  = eng[0:-1]
          
          
            else:
                eng  =  pig[-1:]+pig[0:-1]
                eng  =   eng[0:-1]
       
       
       
        total+=eng+' '
    return total
