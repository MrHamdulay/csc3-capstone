""""Counting Pairs using Recursion
Adam Edelberg
2014/05/09"""

mess = input("Enter a message:\n")



def pair(mess):
    if len(mess) <= 1:
        return 0
    
        
    if (mess[0] == mess[1]):
  
        return 1 + pair(mess[2:])
    else:

        return pair(mess[2:])
    
print ("Number of pairs:", pair(mess))
