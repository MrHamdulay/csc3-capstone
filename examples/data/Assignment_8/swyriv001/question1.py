"""Program to find palindrome
    Rivoningo Seweya
    08 May 2014"""
#write a palindrone
def palicheck(statement):
  if len(statement)==0:
    return True
  elif len(statement)==1:
    return True
  elif statement[0] == statement[len(statement)-1]:
    return palicheck(statement[1:len(statement)-1])
  else:
    return False
#recursion step
statement=input("Enter a string:\n")
pal=palicheck(statement)
 
if pal:
  print("Palindrome!")
else:
  print("Not a palindrome!")