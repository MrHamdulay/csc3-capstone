#Amitha Doodnath - DDNAMI001
#08/05/2014
#Programme to encrypt a message by converting all lowercase characters to the next character

def convert(word):
    if word=="" or word.isupper():
        return word
    
    else:
        letter=word[:1]
        if (not letter.isalpha()) or letter==" ":
            return letter+ convert(word[1:])
        elif letter=="z":
            return "a"+ convert(word[1:])
        else:
            x=ord(word[:1])
            uniVal=x+1
            return chr(uniVal)+ convert(word[1:])


def main():
    msg=input("Enter a message:\n")
    wordConvert=convert(msg)
    print("Encrypted message:")
    print(wordConvert)
    
main()