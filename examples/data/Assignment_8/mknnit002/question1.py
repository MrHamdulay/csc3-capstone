#mknnit002
#ass 8 question 1
#palindrome

def palindrome(string):
    
    if len(string)<2:
        return True
    elif string[0]==string[-1]:
            return palindrome(string[1:-1])
    else:
        return False
    
def main():
    x=input("Enter a string:\n")
    if palindrome(x)==True:
        print("Palindrome!")
    else:
        print ("Not a palindrome!")
        
main()
