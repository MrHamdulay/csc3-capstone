""" Bella Gorham 
palindrome sentence checker
06/05/14"""

    
# define a function    
def palindrome(string):
    #check if length too small to use splitting and do these explicitly
    if len(string) == 2 and string[0] == string[1]:
        return True
    if len(string) == 1:
        return True
   #if the beg = end run again testing one less from the front and back
    if string[0] == string[len(string)-1]:
        
        return palindrome(string[1:len(string)-1])
    
    return False


    
# define function to run with inputs
def main():
    sentence = input("Enter a string:\n")

    if palindrome(sentence) == True:
        print("Palindrome!")
    else: 
        print("Not a palindrome!")


main()


       
    