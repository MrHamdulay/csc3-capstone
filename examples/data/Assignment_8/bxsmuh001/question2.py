#Assignment 8, Question 2
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 08/05/2014

#This program is designed to check pair of characters in a string.
#Pre-condition: Input string.
#Post-condition: Output number of pairs of characters.

#Creating a recursive function to find pair of characters in string.
def charPair(word,count=0): #Initialize counter to 0.
  if(len(word)>=2): #As long as length is greater than 2 or equal 2
    if(len(word)>2): #If message is greater than 2.
      if(word[0] == word[1] and word[1]==word[2]):
        return charPair(word[2:],count+1) #If first character equals second character add 1 to counter.
      elif(word[0] == word[1] and word[1] != word[2]):
        return charPair(word[1:],count+1)
      else:
        return charPair(word[1:],count+0)
    #If Message is exactly of length 2.
    elif(len(word) == 2):
      if(word[0] == word[1]):
        return charPair(word[2:],count+1)
      else:
        return charPair(word[1:],count+0)
  else: #If word has less than 2 characters.
      return count #Return total count(i.e. pair of characters)


#Checking if this file is being run as a standalone.
if __name__ == '__main__':    
  userInput = input("Enter a message:\n")  
  print("Number of pairs: ", charPair(userInput,count=0), sep="")
