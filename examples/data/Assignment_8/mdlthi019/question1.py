"""Program with recursion to check if a string is a palindrome
Thiloshni Moodley
7 May 2014"""

#user asked to enter a string
string = input("Enter a string:\n")

def string_palindrome(string):
        if string[0] == string[len(string)-1] and len(string) <= 3:#if the string length is less than or =3 and the last and first character equal
                print("Palindrome!")  #string is a palindrome  
        elif string[0] == string[len(string)-1]: #When the length of string is more than 3 characters long and first and last letter same
                return string_palindrome(string[1:len(string)-1]) #Take away first and last letter        
                    
        else: #When the first and last characters are not the same
                print("Not a palindrome!")
                
if __name__=="__main__":
        string_palindrome(string)
                        
        