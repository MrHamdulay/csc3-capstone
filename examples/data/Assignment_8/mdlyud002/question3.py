#Yudhi Moodley 
#Assignment 8 - Recursive function to encrypt a message
# 09/05/2014

#store the alphabet in a list
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encryptedString = []
def encryptMessage (rope):
    
    # proved base case
    if rope == '':
        return 0
     
    # 'z' changes to 'a' not just end
    elif rope[0] == 'z':
            encryptedString.append('a')
            return encryptMessage (rope[1:])
        
    elif rope[0] in alphabet:
                position = alphabet.index(rope[0]) + 1
                encryptedString.append(alphabet[position])
                return encryptMessage (rope[1:])
            
    else:
        # not in lower case add string and recur.
        encryptedString.append(rope[0])
        return encryptMessage (rope[1:])

message = input("Enter a message:\n")

encryptMessage (message)

print("Encrypted message:")
print(''.join(encryptedString))