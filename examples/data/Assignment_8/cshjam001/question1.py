"""Check for palindrome
James Cushway
06-05-2014"""
count = 0
word=input('Enter a string:\n')
def palindrome(count):
    if count<=len(word)//2:
        x=word[len(word)-1-count]
        if x==word[count]:
            count+=1
            palindrome(count)
            if count==len(word)//2:
                print('Palindrome!')
            
        
        else:
            print('Not a palindrome!')
    
palindrome(count)
            
   
    
   