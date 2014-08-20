#piglatin
#remove first consonent and add it to the end and then add an ay suffix
#if the word begins with a vowel, "way" should be appended (example: apple becomes appleway)
#if the word begins with a sequence of consonants, this sequence should be moved to the end, prefixed with "a" and followed by "ay" (example: please becomes easeaplay)
def toPigLatin(s):
    #sentence
    output=""
    myList = s.split(" ")
    tracker=0
    listLen = len(myList)-1
    for word in myList:
        con=''
        count =True
        
        if 'aeiouAEIOU'.find(word[0:1])>=0:
            output += word+'way'
            
        else:
            for i in word:
                if 'aeiouAEIOU'.find(i)>=0 :
                    count= False
                if 'aeiouAEIOU'.find(i)<0 and count==True:
                    con+=i
                else:
                    output+=i
                
            output=output+'a'+con+'ay'
        
        #print(output)
        if(tracker<= listLen):
            output+=" " 
        count= True
        tracker+=1
    return output


def toEnglish(s):
    output=""
    myList = s.split(" ")
    tracker=0
    listLen = len(myList)-1  
    for word in myList:
        con=''
        rest=''
        #count =True
        if word[len(word)-3:]=='way':
            output += word[:len(word)-3]+" "
        else:
            for i in range(len(word)-3,0,-1): 
                if word[i]=='a':
                    rest = word[:i]
                    break
                if  word[i]!='a':
                    con+=word[i]
            output=output+ con[::-1]+rest+" "
                
    #This one takes the last consonent and puts it in the front and removes the ay
    #s = s[:len(s)-2]
    return output
