#maisha ivha 
#10 May 2014
#CREATING OF PROGRAMME THAT USES RECURSIVE FUNCTION TO CONVERT A STRING TO AN ENCRYPTED STIRNG


def encrypt(word):
    if word ==" "or word=="":#the programme should return an empryt string if there input is empry string
        return" "
    
   
    else:

        uni= ord(word[:1]) +1 #if the string is not empty the unicode of the character is increminated by 1 to make it the next alphabet

        letter= chr(uni) #converting the unicode to the alphabet
        if word[0] < chr(97):#if the character is any other than an alphabet alike a full stop the programe should leave it as it is
                        letter = word[0]        

        elif (ord(word[:1]) == 32):

            letter = chr(uni-1) 

        else:

            if word[:1] == 'z': #if the character is "z", the programme should change it to "a"

                letter='a' 
                

            else:

                letter= chr(uni)

        

        print (letter,end='')

        return encrypt(word[1:])
    
def main():
    word = input("Enter a message:\n")
    print('Encrypted message:')
    
    print(encrypt(word))
main()

        