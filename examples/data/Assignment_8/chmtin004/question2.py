"""program to check paired characters using recursion
Tinotenda Chemvura CHMTIN004
03 May 2014"""

#__________________________Program Starts Here__________________________________

def check_pairs(msg):
    #check if the string is at least 2 characters long, if true return 0
    if len(msg) < 2:
        return 0
    #check if the 1st character == to 2nd character, if true, return 1 + the string with the 1st character in the in sliced off to the function, if false, return 0 + the string with the 1st character in the in sliced off to the function.
    else:
        if msg[0] == msg[1]:
            return 1 + check_pairs(msg[2:])
        else: return 0 + check_pairs(msg[1:])
#print the results    
msg = input("Enter a message:\n")
print("Number of pairs:",check_pairs(msg))
#___________________________Program Ends Here___________________________________