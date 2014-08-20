""" Question 2 - Character pairs checker
Tauhirah Eguardo
2014/05/04"""
def main():
     msg = input("Enter a message:\n")
     pairs = 0
     pairer(msg,pairs)
     
      
def pairer(msg,pairs):
     
     if len(msg) <= 1:
          return print("Number of pairs:",pairs)
     else:
          if msg[0] == msg[1]:
               pairs+= 1
               msg = msg[2:]
               
          else:
               msg = msg[1:]
           
          return pairer(msg,pairs)
     
main()
          
     