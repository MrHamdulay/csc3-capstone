#To convert from English to Pig Latin, each word must be transformed as follows:
#
#if the word begins with a vowel, "way" should be appended (example: apple becomes appleway)
#if the word begins with a sequence of consonants, this sequence should be moved to the end and followed by "ay" (example: please becomes easeplay)
#Assume that the English text does not contain the letter "w".
#
#Write a Python module with the following functions:
#
#toPigLatin (s), to return the Pig Latin string for a given English string
#toEnglish (s), to return the English string for a given Pig Latin string

import re
def toPigLatin(s):
    x=0;
    latin=""
    while (x!=-1):
        x=s.find(" ")
        if (x!=-1):
            temp=s[0:s.find(" ")]
            s=s[s.find(" ")+1:]
        else:
            temp=s
            s=""
        if (temp[0].lower=="a" or temp[0].lower=="e" or temp[0].lower=="i" or temp[0].lower=="o" or temp[0].lower=="u"):
            temp=temp+"way"
            if(x!=-1):
                latin=latin+temp+" ";
            else:
                latin=latin+temp
        else:
            vows=["a","e","i","o","u"]
            pos=len(temp)
            for i in range(5):
                itr=temp.find(vows[i])
                if(itr!=-1 and itr<pos):
                    pos=itr
                    
            if (pos!=0):
                end="a"+temp[0:pos]+"ay"
            else:
                end=temp[0:pos]+"way"
            temp=temp[pos:]+end
            if(x!=-1):
                latin=latin+temp+" ";
            else:
                latin=latin+temp            
            
    return latin     


def toEnglish(s):
    x=0
    english=""
    while (x!=-1):
        x=s.find(" ")
        if (x!=-1):
            temp=s[0:s.find(" ")]
            s=s[s.find(" ")+1:]
        else:
            temp=s
            s=""
                  
        if (temp.find("way")==len(temp)-3):
            temp=temp[0:-3]
            english =english +temp
        else:
            temp=temp[0:-2]
            
            a=0
            search=temp
            
            for j in range (len(search)):
                if(search[j]=="a"):
                    a=j
               
            
            
            temp=temp[a+1:]+temp[0:a]
            english=english+temp
        
        if(x!=-1):
            english=english+" "
        
    return english
        
        
        

    
                    
                    
    
            
            
            