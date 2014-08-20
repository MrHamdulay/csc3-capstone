#Recursive program to encrypt a string
#Tyrone Arnold
#9 May 2014


alphabet_string='abcdefghijklmnopqrstuvwxyz'#string of the alphabet indexed from 0
encrypt_string='' #empty string to be filled with encrypted string
position=0 #letter number to encrypt

def encrypt(position):
    global encrypt_string #calls the empty string from outside the function
    
    if string[0] not in alphabet_string[::]: #if first letter is capitalized
        encrypt_string = string    # do not encrypt
    elif position<len(string) and string[position] == ' ': #if space replace with space
        encrypt_string+=' '
        return encrypt(position+1) #recurse on next position
    
    elif position<len(string): #if position (index) is within the string
        if string[position] != "z": #if letter is not z
            encrypt_string+=(alphabet_string[alphabet_string.find(string[position])+1]) #replace with letter indexed to position plus 1
            return encrypt(position+1) #recurse on next position
        elif string[position] == "z": #if letter is z
            encrypt_string+=(alphabet_string[alphabet_string.find(string[position])-25]) #replace with a

string=input('Enter a message:\n') #input outside the function

encrypt(position) #calls function after input
#function runs
print('Encrypted message:\n',encrypt_string,sep='') #print encrypted string