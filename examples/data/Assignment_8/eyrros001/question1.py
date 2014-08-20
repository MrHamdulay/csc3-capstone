"""Check if string is pallindrome
Ross Eyre
04/05/2014"""

length = 0

def main():
    sent = input("Enter a string:\n")
    length = len(sent)
    if(palindrome(sent)):
        print("Palindrome!")
    else: print("Not a palindrome!")
    

def palindrome(string):
    l = len(string)
    
    if(l==0 or l==1):
        return True      
    elif (string==reverse(string)):
        return True
    else:
        return False

def reverse(string):

    if (len(string) <= 1):
        return string
    
    return reverse(string[1::]) + string[0:1:]    

main()
   

