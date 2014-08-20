'''This program encrypts a message by converting all alphabetical lowercase characters to the
 next character cyclically
 By Hermann KOUASSI: KSSKOU001
 On 3 May 2014'''

#create an empty string to store encrypted message
encr_mes = ''

def encry(message):
    '''encrypt a given message'''  
       
    #stopping condition and in case empty string entered
    if message =='' :
        #call global variable above
        global encr_mes
        print('Encrypted message:\n',encr_mes,sep='')
    #do not encrypt non alphabetical character
    elif not message[0].isalpha():
        #add same character to encrypted message
        encr_mes += message[0]
        #call encry function for recursion leaving out the first character 
        encry(message[1:])
    #encrypt 'z' as 'a': 
    elif message[0]=='z':
        encr_mes += 'a'
        encry(message[1:])
    #when string not empty
    else:
        #change the first character by the one which follows it in alphabetical order
        if message[0].isupper():
            #if upper character keep the same character
            encr_mes += message[0]
        else:
            encr_mes += chr(ord(message[0])+1)
        #continue the recursion with first character out
        encry(message[1:])

def main():
    '''main function to get input'''
    
    message = input('Enter a message:\n')
    encry(message)
    
if __name__=="__main__":
    main()