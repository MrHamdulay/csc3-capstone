#Siphesihle Cele
#10 May 2014
#assignment 8

#recursive function that reads encrypted messages 
#then replacing the letter with the next one on the alphabets.
#o0ndenting the letter with n+1, where n is its position between 1-26 alphabets.
#main function once again, requesting encrypted message and printing out the indented message
def encrypt(user_input):
    if user_input =='':
        return ''   
    else :
        if user_input[0] == 'z':
            coversion = chr(ord('z') - 25)
            return a +encrypt (user_input[1::])
        elif user_input[0] == ' ':
            conversion = ' '
            return conversion + encrypt (user_input[1::])
        else:
            conversion = chr(ord(user_input[0])+1)
            return conversion+encrypt (user_input[1::])
def main():
    user_input=input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(user_input))
main()