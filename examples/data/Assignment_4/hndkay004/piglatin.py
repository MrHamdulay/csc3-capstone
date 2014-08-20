def toPigLatin(s):
   vowels=['a','e','i','o','u','A','E','I','O','U']
   s=s.split()
   x=''
   for i in s:
      if i[0] in vowels:
         i=i+'way'
         x=x+i+' '
      else:
         i=i+'a'
         while i[0] not in vowels:
            i=i[1:]+i[0]
         i=i+'ay'
         x=x+i+' '
   return x
   
def toEnglish(s):
   s=s.split()
   x=''
   for i in s:
      if i[-1:-4:-1]=='yaw':
         i=i[0:len(i)-3]
         x=x+i+' '
      else:
         i=i[0:len(i)-2]
         while i[-1]!='a':
            i=i[-1]+i[0:len(i)-1]
         i=i[0:len(i)-1]
         x=x+i+' '
   return x
    
    