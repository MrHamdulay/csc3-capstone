"""Count pairs of characters
B.Player
04/05/2014"""

def pairs(s):
   """Counts number of pairs of repeated characters in a string"""   
   if len(s)==1: return 0
   elif len(s)==2 and s[0]==s[1]: return 1
   elif s[0]==s[1] and s[1]!=s[2]:
      return 1+pairs(s[1:])
   elif s[0]==s[1]==s[2]: return 1+pairs(s[2:])
   else: return pairs(s[1:])
   
st=input("Enter a message:\n")
print("Number of pairs:",pairs(st))