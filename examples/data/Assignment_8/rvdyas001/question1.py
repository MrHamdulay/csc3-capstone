string=str(input("Enter a string:\n"))

def palin(s): 
   if len(s)%2==0 and s[0:len(s)]==s[::-1]:
      print("Palindrome!")
   elif len(s)%2!=0 and s[0:(len(s)//2)]==s[:(len(s)//2):-1]:
      print("Palindrome!")
   else :
      print("Not a palindrome!")
    
palin(string)
