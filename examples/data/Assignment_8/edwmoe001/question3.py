""" Question 3 -- encrypterer
Tauhirah Eguardo
2014/08/04"""

def main():
     msg = input("Enter a message:\n")
     str_number= 0
     amount = len(msg)
     encrypter(msg,str_number,amount)
     
def encrypter(msg,str_number,amount):
     
     
     if str_number == amount:
          
          return print("Encrypted message:\n",msg[amount:],sep="")
     else:
          
          if msg[str_number] == "z":
               new = "a"
          elif msg[str_number].islower():
               #print(msg[str_number])
               new = chr(ord(msg[str_number])+1)
               #print(new)          
          else:
               new = msg[str_number]
          msg = msg + new
          str_number += 1
           
          return encrypter(msg,str_number,amount)
main()
          