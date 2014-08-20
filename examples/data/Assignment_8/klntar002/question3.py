# tarisai kalinde
# klntar002
# code to encrypt a message recursively

string=input('Enter a message:\n')
#string=','.join(string)  # inserting commas
#array=string.split(',')   # splitting by commas in2 array
finale=''
def encrypt(string,finale):
    
    # base case
    if string=='':
        return 'Encrypted message:\n'+finale
    else:
        
              
        if string[0].islower() and string[0]!='z': # condition for lower case  letters which are not 'z'
            
            finale=finale + chr(ord(string[0])+1)
            return encrypt(string[1:],finale)      # recursive step
        elif string[0]=='z':                       # condition for letter 'z'
            finale=finale+'a'                      
            return encrypt(string[1:],finale) 
        elif string[0].isupper() :                 # condition for upper case letters
            finale=finale+string[0]
            return encrypt(string[1:],finale)
        else:
            finale=finale+string[0]                # condition for non alphabetical characters
            return encrypt(string[1:],finale)
        
        
        
            
# a product of Tarisai Stephen Kalinde the second #beastmode CSC1015                        
        
       
        
print(encrypt(string,finale))        
            
    
    
