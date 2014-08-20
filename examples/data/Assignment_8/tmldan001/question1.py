'''Program with a recursive function to calculate whether or not a string is a palindrome
Daniel M. Tamale
TMLDAN001
2014-05-06'''
 
def palindrome(word):
 '''To reverse word and check if its a palindrome'''
 if len(word)<2:
  return True
 elif word.isupper():
  return False
 elif word[0] == word[-1]:
   return palindrome(word[1:len(word)-1])
 else:
  return False
 
def main():
 '''To print palindromes and non palindromes'''
 word=input('Enter a string:\n')
 if palindrome(word)==True:
  print ('Palindrome!')
 else:
  print('Not a palindrome!')
main()