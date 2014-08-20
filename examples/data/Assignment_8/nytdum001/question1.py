""" Program to check if a string is a palindrome or not using recursion
Dumisani J Nyathi
09-05-2014"""


def rev_string(string):
   if string == '':#if string gets to this point then it means all the other letters passed comparison since the string is now empty
      print("Palindrome!")
   elif (ord(string[0]) == ord(string[len(string)-1])):
         return rev_string(string[1:len(string)-1]) #will re-invoke rev_string function for next letter and so on  
   else:
      print("Not a palindrome!")
      
def palin_check():
   #to get string to be checked
   string = input("Enter a string:\n")
   
   #to make letters all lowercase for comparison
   string = string.lower()
   
   rev_string(string)#invoke function to check for palindrome
   
palin_check()