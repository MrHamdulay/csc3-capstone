def palin(word):
    output = '' 
    
    if len(word) < 2:
        output = 'Palindrome!'
        return output
    
    if word[0] != word[-1]:
        output = 'Not a palindrome!'
        return output
    
    return palin(word[1:-1]) 

#==========================================

test = input('Enter a string:\n')

out = palin(test)

print(out)