# Alex Brunette
# 08/05/2014
# Program to encrypt a message
word= input("Enter a word:\n")
def encrypt(word):
    if word[0]=='':
        return ''
    if word[0] == ' ':
        return ' '
    if 121 >= ord(word[0]) >= 97:
        original_char= ord(word[0])
        encrypt_char= original_char +1
        return chr(encrypt_char) + encrypt(word[1:len(word)])
def main():
    x=encrypt(word)
    print(x)   
        
main()          
    