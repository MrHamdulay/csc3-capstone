#Eng to Pig



def toPigLatin(s):
    
    nay='w'
    word=s.split(' ')
    space=""
    
    for q in range(len(word)):
        wrd=word[q]

        if nay in wrd:
            None
        else:
            upper = "AEIOU"
            lower = "aeiou"
            
            if wrd[0:1] in upper or wrd[0:1] in lower:
                wrd+='way'
                

            else:
                
                acc=0
                for i in range(len(wrd)):

                    if wrd[i] not in upper and wrd[i] not in lower:
                        acc=acc+1
                        continue

                    else: break
                    
                wrd=wrd[acc:]+'a'+wrd[0:acc]+'ay'

        space+=wrd+' '

    return space[:-1]







#Pig to Eng

def toEnglish(s):
    word = s.split(' ')
    space = ""
   
    for h in range(len(word)):
        wrd = word[h]
        

        if wrd[:-4:-1] == "yaw":
            wrd = wrd[:-3]


        else:
            wrd = wrd[:-2]
            acc = 0

            for m in wrd[::-1]:

                if m=='a':
                    wrd=wrd[len(wrd)-acc:]+wrd[:len(wrd)-acc-1]
                    break

                else:
                    acc+=1


        space += wrd+' '

    return space[:-1]
