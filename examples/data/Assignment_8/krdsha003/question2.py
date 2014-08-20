""" Assignment 8 Question 2
count the number of pairs of repeated characters in a string
Shaheen Karodia
KRDSHA003
2014-05-04"""


def pairs(string):
    """counts the number of pairs of repeated characters in a string without overlaps"""
    
    if len(string)< 2 : #base case, if there are less than two characters in a string there can be no pairs 
        return 0
    elif string[0]!=string[1]:  #checks if the first and seond character are the same
        
        return pairs(string[1:])  #recurses through a string without the first character 
    
    else:
        
        return  1+ pairs(string[2:])  #recurses through a string without the first two characters 
    
    
def main():
    x=input("Enter a message:\n")
    print ("Number of pairs:", pairs(x))    
    
main()
    
    
  