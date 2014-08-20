"""Encrypt a message
B.Player
04/05/2014"""

def encrypt(mes):
   """Encrypts a message, all lowercase shifted one letter in alphabet, z to a"""
   if len(mes)==1: 
      if mes.islower() and mes!='z': return chr(ord(mes)+1)
      elif mes=='z': return 'a'
      else: return mes
   elif mes[0].islower() and mes[0]!='z': return chr(ord(mes[0])+1)+encrypt(mes[1:])
   elif mes[0]=='z': return 'a'+encrypt(mes[1:])
   else: return mes[0]+encrypt(mes[1:])
   
   
   
mes=input("Enter a message:\n")
print("Encrypted message:\n"+encrypt(mes))