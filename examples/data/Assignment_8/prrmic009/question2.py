"""Program to count the number of pairs of repeated characters in a string
Mick Perring
07 May 2014"""

message = input("Enter a message:\n")   # user inputs message
n = 0
k = 0

def rep(message, k, n):   # rep function to check for and count pairs of repeated characters in string
    check1 = k
    check2 = k + 1
    if check2 >= len(message):        # ends function running when whole string has been checked
        print("Number of pairs:", n)  # and prints count of pairs of repeated characters
        return
    
    if message[check1] == message[check2]:  # adds to count if pair is found
        n += 1
        rep(message, k + 2, n)
        
    else:                           # repeats function until string has been completely checked
        rep(message, k + 1, n)
        
rep(message, k, n)