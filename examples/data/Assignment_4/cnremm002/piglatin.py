def toPigLatin(messageP):
    
    message = ""
    index = 0
    
    for i in range (len(messageP)):
        
        if messageP[i]==" " or i == (len(messageP)-1):  
            if i == (len(messageP)-1):
                tempWord = messageP[index:i+1]
            else:
                tempWord = messageP[index:i]
                
            if tempWord[0] == 'a' or tempWord[0] == 'e' or tempWord[0] == 'i' or tempWord[0] == 'o' or tempWord[0] == 'u':
                tempWord += "way"
                message += tempWord+" "
                
            else:
                t=0
                for j in range(len(tempWord)):
                    if tempWord[j] == 'a' or tempWord[j] == 'e' or tempWord[j] == 'i' or tempWord[j] == 'o' or tempWord[j] == 'u':
                        tempWord = tempWord[j:]+'a'+tempWord[0:j]+'ay'
                        message += tempWord+" "
                        break
                    else:
                        t+=1
                    if(j==(len(tempWord)-1)):
                        tempWord = "a"+tempWord+"ay"
                        message+=tempWord+" "
                        
                        
            index = i+1
                 
    return message
           
           
def toEnglish(messageP):
    message = ""
    index = 0
    
    for i in range (len(messageP)):   
        if messageP[i]==" " or i == (len(messageP)-1):  
                    if i == (len(messageP)-1):
                        tempWord = messageP[index:i+1]
                    else:
                        tempWord = messageP[index:i]
                        
                    if tempWord[-3] == 'w':
                        tempWord = tempWord[0:-3]
                        message += tempWord+" "
                        
                        
                    else:
                        for j in range(len(tempWord)-3,-1,-1):
                            if tempWord[j] == 'a':
                                front = tempWord[j+1:len(tempWord)-2]                            
                                tempWord = front + tempWord[0:j]
                                message += tempWord+" "
                                break
                                
                    index = i+1
                             
    return message