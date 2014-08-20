#COUNTS REPEATED CHARACTERS USING RECURSION
#MULISA BADUGELA
#9 MAY 2014
def countr(string):
   if len(string) == 0: # base case
      return 0
   else:
      firstletter = string[0:1]  # get first letter of the message typed in by user

      if firstletter == string[1:2]: 
         return 1 + countr(string[2:]) # recursive step, 
      else:
         return countr(string[1:])

message = input("Enter a message:\n")
print("Number of pairs:",countr(message))