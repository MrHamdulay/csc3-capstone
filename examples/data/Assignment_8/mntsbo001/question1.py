"""Program to check if string is a palindrome
Sbonelo Mntungwa
9 May 2014"""


def palndrm(string):                         #Defining function 
   if len(string) == 1 or len(string) == 0:  #When there is only one or no character left in string
      print( "Palindrome!")                  #output result
   else:
      if string[0] == string[-1]:            #First letter equals to last letter
         return palndrm(string[1:-1])        #string returned without first and last letter
      else:
         print( "Not a palindrome!")         #output result
     
    
    
    
string =input("Enter a string:\n")           #entering the string
palndrm(string)                              #running the function