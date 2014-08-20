#Nasiha Ally
#ALLNAS012  
#May 2014


 
    
def pal(string):
   if (string): 
      if (string[0] == string[-1]):
         result =pal(string[1:-1])
         
         if result:
            return True
   else:
      return True    
   return False

if __name__ == "__main__":
   x = input("Enter a string:\n")
   result = pal( x )
   
   if not result:
      print("Not a palindrome!")
   else:
      print("Palindrome!")

