"""program to encryt a message by converting all lowercase characters to the next character
vicky stark
8 may 2014"""

def code(words):
    if len(words)==0:
        return words
    if words.isupper():
        return words 
    if words[0]==' ' or words[0]=='.':
        return words[0]+code(words[1:])#if there is a space you want it to print the space but continue onto the next word
    if words[0]=='z':
        return 'a'+code(words[1:])
    else: 
        return chr((ord(words[0]))+1) + code((words[1:])) #use ord and chr to get the unicode value and add one
        
words=input("Enter a message:\n")
returned_words=code(words)
print("Encrypted message:\n"+returned_words)
