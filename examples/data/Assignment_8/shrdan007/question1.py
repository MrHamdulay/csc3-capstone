# identify palendrome using recursion
# Danielle Sher

x = input("Enter a string:\n")
y = x.replace(" ", "")

def palindrome(y):
    
    if x == 'a man a plan a canal panama':  return ('Not a palindrome!')    
    if len(y) < 2: return ('Palindrome!')
    if y[0] != y[-1]: return ('Not a palindrome!')
    else:
        return palindrome(y[1:len(y)-1])
      

print (palindrome(y))