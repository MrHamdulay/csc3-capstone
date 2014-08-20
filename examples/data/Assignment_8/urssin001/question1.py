#Write a Python program with a recursive function to calculate whether or not a string is a palindrome (reads the sa me if reversed).
#Sinead Urisohn
#6 May 2014

#get input
s=input("Enter a string:\n")
#create recursive function to determine palindrome that receives string as parameter
def pal_str(s):
       #base case is when string empty
       #return False
       if s=="":
              return False
       else:
              #if first character not = to last character, string not palindromic: return False
              if s[0]!=s[-1]:
                     return False
              #if string still has more than 2 characters to compare
              elif len(s)>2:
                     #repeat recursive step by chopping off first and last characters 
                     return pal_str(s[1:-1])
              
#display results
if pal_str(s)==False:
       print("Not a palindrome!")
else:
       print("Palindrome!")
       