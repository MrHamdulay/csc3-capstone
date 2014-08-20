# Determins if a string is a palindrome
# Conor O'Sullivan
# 04/05/2014

#input string
sent = input("Enter a string:\n")

#recursive Function
def palin(sent):
       
       if len(sent) == 1 or len(sent) == 0:
              print("Palindrome!")
       elif sent[0] != sent[len(sent)-1]:
              print("Not a palindrome!")
       else:

              return palin(sent[1:len(sent)-1])
  
palin(sent)
       