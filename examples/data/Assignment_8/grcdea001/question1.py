"""program to determine if a sentance is a palindrome or not, recursivly
Dean Gracey
4 May2014"""

def palindrome(word):
    
   if len(word)<2:
      print("Palindrome!")
      return
   
   
   first = word[0]
   last = word[len(word)-1]
   
   
   if (first==" ") :
      first = word[0]
      word= word[1:len(word)]
      
      
      
   if(last==" ") :
      last = word[len(word)-1]
      word = word[0:len(word)-1]
      
      
   if first!=last:
      print("Not a palindrome!")    
         
   else:
      return palindrome(word[1:len(word)-1])
   
     
word = input("Enter a string:\n")

if len(word)>0:
   
   palindrome(word)
