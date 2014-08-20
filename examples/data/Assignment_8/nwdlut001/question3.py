message=input("Enter a message:\n")
def change(n):
   if n=="z":
      s="a"
      print(s,sep="",end="")
   else:
     s=ord(n)
     r=s+1
     f=chr(r)
     print(f,sep="",end="")
print("Encrypted message:")
def upper(message):
   if message==message.upper():
      print(message)

def newone(message):
   if message==message.lower():
      if message=="":
         return message
      else:
          return str(change(message[0]))+(newone(message[1:]))
newone(message)
upper(message)
