"""Palindrome check
B.Player
04/05/2014"""

def palin(s):
   """Checks if a string is a palindrome, returns boolean"""
   if s=='': return True
   elif s[0]==s[-1]:
      return palin(s[1:-1])
   else: return False
   
if __name__ == '__main__':
   s = input("Enter a string:\n")
   if palin(s):   
      print("Palindrome!")
   else: print("Not a palindrome!")