"""Assignment 8-Q1
Nandani Birjanund
5 May 2014"""

string_by_input=input("Enter a string:\n") #user inputs a palindrome or non palindrome
def Pal(string_by_input):
   if string_by_input =="": #empty str
      return "" #gives an empty str
   
   elif string_by_input==" ": #or there is an input with space
      return " "  #returns a space
   
   else:
      return string_by_input[-1] + Pal(string_by_input[0:len(string_by_input)-1]) #users string backwards to see if a palindrome using the len function and string slicing
    
function=Pal(string_by_input) 

if function==string_by_input:
   print("Palindrome!") #yes palindrome
else:
   print("Not a palindrome!") #not a palindrome