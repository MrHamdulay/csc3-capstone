"""a program that counts the number of pairs of repeated characters in a string
nelisile mkhwebane
07 May 2014
assignment 8, question 2"""

""" getting the message from the user"""
message = input ("Enter a message:\n")
count = 0
def pair_count(s):
    """ to check if the len of the string is less than two characters"""
    if len(s) == 0 or len(s) ==1:
        return 0
    else:
        """check if the first character is equal to the second character"""
        if s[0] == s[1]:
            return (count+1) + pair_count(s[2:])
        else:
            return count + pair_count(s[1:])
    """printing out the number of pairs"""
print ("Number of pairs:",pair_count(message))
