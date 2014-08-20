sample = input("Enter a string:\n")
def palindrome(sample):
    if len(sample)==1 or len(sample)==0:
        return True
    elif sample[0] == sample[-1]:
        return palindrome(sample[1:len(sample)-1])
    else:
        return False
if palindrome(sample) == True:
    print("Palindrome!")
else:
    print("Not a palindrome!")
    
    