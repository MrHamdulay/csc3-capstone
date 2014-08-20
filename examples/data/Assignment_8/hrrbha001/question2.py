def countpairs ( str ):
   if len(str) < 2:
      return 0
   elif str[0]==str[1]:
      return 1 + countpairs (str[2:])
   else:
      return countpairs (str[1:])      

str = input ("Enter a message:\n")
print ("Number of pairs:",countpairs (str))




