def toPigLatin (s):
    Vowels = ['a','e','i','o','u','A','E','I','O','U']
    s= s.split()
    pig=""
    for i in (s):
        if i[0] in Vowels:
            i = i +'way'
            pig+=i +" "
            
        else:
            i=i+'a'
            while i[0] not in Vowels:
                i = i[1:] + i[0]
            i+='ay'
            pig+=i +" "
        
    return pig 



def toEnglish (s):
    s=s.split()
    English=""
    for i in s:
        if i[-1:-4:-1] == 'yaw': 
            i = i[0:len(i)-3]
            English+=i+" "
        else:
            
            i = i[0:len(i)-2]
            while i[-1] != 'a':
                i = i[-1] + i[0:len(i)-1]
            i = i[0:len(i)-1]
            English+=i + " "
            
    return English


        
    



                
            
        
        
            


        
