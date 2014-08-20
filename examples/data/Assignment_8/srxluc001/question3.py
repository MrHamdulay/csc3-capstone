#lucy Sure 
#SRXLUC001
#Assignement 8


y=input("Enter a message:\n")
def Repeat(y):
              if len(y)==0:
                            return y
              else:
                            letter=y[0]
                            if letter.isalpha() and letter.islower():
                                          letter = chr((ord(letter))+1)
                            return letter + Repeat(y[1:])   
print("Encrypted message:\n",end="")
print(Repeat(y))

#ask user to enter a message
#created a fuction called repeat
#checked to see if the string is empty
#if it is the fuction shuould return an empty string
#else it should check to see if the fist letter is an alphabet and is lower
#it should do this for every letter in the string