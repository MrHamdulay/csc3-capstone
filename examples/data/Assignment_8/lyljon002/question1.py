#9 May 2014
#Program to detect whether input is a palindrome or not
#LYLJON002

def pal(text):                              #function to test
    if len(text) == 1 or text == '':
        return True                    #if one character or empty then its a palindrome
    last = text[-1]
    first = text[0]
    if first == last:                   #check first and last letters
        return pal(text[1:-1])      #return string with first and last letters removed, repeat function
    return False

text = input("Enter a string:\n")    

if pal(text)==True:    
    print("Palindrome!")                    #run the test and output results
    
else:
    print("Not a palindrome!")
