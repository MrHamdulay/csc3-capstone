'''Program to encrypt message
   Denzel Ncube
   04 May 2014'''

#Function to remove first character from string
def Removefirst(string):
  lst = list(string)
  del lst[0]
  newstring = "".join(lst)
  return newstring

#Function to encrypt message
def Encrypt(string):
  if string == "":
    return ""
  else:
    #Moving the characters 1 up if lowercase
    if string[0].isalpha() == True and string[0] != 'z' and string[0].islower() == True:
      return chr(ord(string[0])+1) + Encrypt(Removefirst(string))
    #Doing the same for z
    elif string[0].isalpha() == True and string[0] == 'z' and string[0].islower() == True:
      return chr(ord(string[0])-25) + Encrypt(Removefirst(string))
    elif string[0].istitle() == True:
    #Keeping the capital letters the same
      return string[0] + Encrypt(Removefirst(string))
    #Dealing with spaces and punctuation
    elif string[0].isalpha() == False:
      return string[0] + Encrypt(Removefirst(string))
     

#Displaying
Message = input("Enter a message:\n")
print("Encrypted message:")
print(Encrypt(Message))