word = input("Enter a message:\n")
word2=""
def encryption(word,word2):
    if(word.isupper()):
        return word
    else:
        if (word!=""):
            if(word[0:1]!=" "):
                if(word[0:1]=="z"):
                    word2+=("a")
                    return encryption(word[1:],word2)
                elif(word[0:1]=="."):
                    word2+="."
                    return encryption(word[1:],word2)
                else:
                    word2+=(chr(ord(word[0:1])+1))   
                    return encryption(word[1:],word2)
            else:
                word2+=" "
                return encryption(word[1:],word2)
                
        else:
            return word2
        if(word[0:1]==" "):
            return encryption(word[1:],word2)
    


   
print ("Encrypted message:\n",encryption(word,""),sep="")
