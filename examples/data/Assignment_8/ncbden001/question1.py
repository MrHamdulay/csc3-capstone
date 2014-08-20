#Program for checking palindromes
#Denzel Ncube
#03 May 2014

#Function to remove the last character
def Removelast(string):
  lst = list(string)
  del lst[-1]
  newstring = "".join(lst)
  return newstring

#Function To Reverse elements
def Palindrome(string):
  allstring = str(string)
  if allstring == '':
    return allstring
  else :
    return allstring[-1] + Palindrome(Removelast(allstring))
#Getting input
inputstring = input("Enter a string:\n")

#Checking if forward = reverse and displaying result
if str(inputstring)== Palindrome(inputstring):
  print('Palindrome!')
else:
  print('Not a palindrome!')