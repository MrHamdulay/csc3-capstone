# Yentl Naidu (NDXYEN001)
# 8 May 2014
# Assignment 8
# Question 2 - Pairs of the same letter

def pairs(s,p):
  if (len(s)>=2): # When there are more than 2 characters
    if (s[0]==s[1]): # If the two adjacent characters are the same
      return pairs(s[2:],p+1) # Recursive step
    
    else:
        return pairs(s[2:],p) # If they are not the same
  elif (len(s)==1):
    return p
  else:
    return p
      
if __name__ == "__main__":
    x = input("Enter a message:\n") # Get the input to use in function
    result = pairs(x,0)
    print("Number of pairs:",result)
    