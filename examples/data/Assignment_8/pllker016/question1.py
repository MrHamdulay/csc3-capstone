# kereshnee pillay
# 7 may
#palindrome strings


def palindrome(string):
# if string lenght is one it is a palindrome    
    if len (string)<=1:
        
        print('Palindrome!')
#check if latter at the front is equal to letter at the back    
    elif string[0]==string[len(string)-1]:
#check if the next letter at the front is equal to the second last letter, and so one
        return palindrome(string[1:len(string)-1])
    else:
        print('Not a palindrome!')

if __name__=='__main__':
    string=input('Enter a string:\n')
    palindrome(string)
    
