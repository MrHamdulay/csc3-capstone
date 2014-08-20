#RYXSHR002
# piglatin program
#4/04/2014




def toPigLatin(s):

    m=''
    
    for i in s.split(" "):
        
        if i[0] in 'aeiou':
            
            m= m+(i+'way ')
        else:
            
            for g in i:
                if g in 'aeiou':
                    
                    m=m + (i[i.find(g):]+'a'+i[:i.find(g)]+'ay ')
                    break
            else:
                
                m=m +('a'+i+'ay ')           
    return m[:len(m)-1]

def toEnglish(s):
    m=''
    reverse=''
    for i in s.split(" "):
        if i[len(i)-3:] == 'way':
            m+=i[:len(i)-3]+' '
        else:
            reverse = i[::-1][2:]
            for g in i:
                if g == 'a':
                    m= m+ ((reverse[reverse.find('a')+1:]+reverse[:reverse.find('a')])[::-1]+' ')
                    break
                
    return m[:len(m)-1]

