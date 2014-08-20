# Recursion
# encrypt a message by converting all lowercase characters to the next character 
# Hendrik Joosten
# JSJOH004
# 04 May 2014


# accept parameters of original string and new string
def encrypt(s,new_s):
      # when the original string has no len the encoding is complete
      if len(s) == 0:
            print("Encrypted message:\n"+new_s)
      # theis part does the encoding
      else:
            # finds the unicode value of the letter
            x = ord(s[0])
            # if the letter is [a,z]
            if 97 <= x and x <= 122:
                  # if the letter is Z change it to a, special case
                  if x == 122:
                        new_s+= chr((x+1)-26)
                        return encrypt(s[1:],new_s)
                  # else just shift the letter one to the right
                  else:
                        new_s+= chr(x+1)
                        return encrypt(s[1:],new_s)
            # iterate the encoded tring by ading the unencryptes letter 
            # if it is a capital letter or a symbol
            else:
                  new_s+= chr(x)
                  return encrypt(s[1:],new_s)

user_str_in = input("Enter a message:\n")
encrypt(user_str_in,"")
      
