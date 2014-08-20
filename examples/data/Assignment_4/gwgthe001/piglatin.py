def toPigLatin (word):
    a=0
    b=0
    output=''
    for i in range(len(word)):
        a= a + word[b:].find(' ')
        if word[b:].find(' ') == -1:
            if word[b] in 'aeiou':
                output+=(word[b:]+'way')
                break 
            else:
                for j in range(len(word[b:])):
                    if word[b+j] in 'aeiou':
                        output+=(word[b+j:]+'a'+word[b:j+b]+'ay')
                        break                    
            break
        elif word[b] in 'aeiou':
            output+=(word[b:a]+'way ')
            a+=1
            b=a            
        else:
            for j in range(len(word[b:a])):
                if word[b+j] in 'aeiou':
                    output+=(word[b+j:a]+'a'+word[b:j+b]+'ay ')
                    a+=1
                    b=a
                    break
    return(output)

def toEnglish(word):
    a=0
    b=0
    output=''
    for i in range(len(word)):
        a= a + word[b:].find(' ')
        if word[b:].find(' ') == -1:
            word = word[b:]
            if word[-3:] == "way":
                        output+=(word[:-3]) + " "
                        break          
            else:
                        new = word[:-2]
                        newword=new[::-1].find('a')
                        newword= len(new) - newword - 1
                        output+=new[newword+1:]+new[:newword] + " "
                        break     
            
        elif word[a-3:a] == "way":
            output+=(word[b:a-3]) + " "
            a+=1
            b=a            
        else:
            new = word[b:a-2]
            newword=new[::-1].find('a')
            newword= len(new) - newword - 1
            output+=new[newword+1:]+new[:newword] + " "
            a+=1
            b=a              
    return output
                    