#Programme using recursion to check if a string is a palindrome
#Joe Stton
#5 May 2014

def check_palindrome(sentence):
    sentence=sentence.lower() #So that "a" is seen the same as "A"
    
    length_of_sentence=len(sentence)
    
    if length_of_sentence== 1 or length_of_sentence==0:
        return True #A string of this length must be a palindrome
    else:
        if sentence[0]==sentence[-1]:
            sentence=sentence[1:length_of_sentence-1]
            return check_palindrome(sentence)
        else:
            return False
        
if __name__=="__main__":
    
    sentence=input("Enter a string:\n")
    if check_palindrome(sentence):
        print("Palindrome!")
    else:
        print("Not a palindrome!")