
def toPigLatin(s):
   
    
    pig = ''
    lista = s.split()
   
    for c in range(len(lista)):
        word =lista[c]
        if word[:1] in 'aeiou':
            
            pig += word[:] +'way' + " "
        else:
            nt = 0
            for c in word:
                if c not in 'aeiou':
                    if nt==len(word)-1:
                        pig += "a" + word + "ay" + " "
                    nt +=1
                else:
                    pig += word[nt:] + "a" + word[:nt] + "ay" +" "
                    break
                
    return pig

def toEnglish(s):
    
    
    Eng = ''
    new_list = s.split()
   
    for i in range(len(new_list)):
        word = new_list[i]
        
        if word[-3:] == "way":
            Eng += (word[:(len(word)-3)] + ' ')
        else:
            string = word[:len(word)-2]
            z = string.rfind('a')
            Eng += string[z+1:]+string[:z] + ' '
          
    return Eng
            
            
        
        