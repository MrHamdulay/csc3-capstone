# Author : Rayaan Fakier FKRRAY001
# Date : 24 - 03 - 2014
# Question 3

def main():
    # Take inputs
    mess = input("Enter the message:\n")
    messrep = int(input("Enter the message repeat count:\n"))
    frme = int(input("Enter the frame thickness:\n"))
    n = 0
    lm = len(mess)
    # Print top frame according to inputs
    for x in range(frme):
        print("|" * x + "+" + "-" * ((frme * 2) + lm - 2 * x) + "+" + "|" * x)
        n+=1
        
        if n == frme: # Prints message when top frame is done
            for i in range(messrep):
                print("|" * (x+1), mess, "|" * (x+1))
        else: 
            continue
    # Print bottom frame by reversing top frame
    for p in range(frme-1, -1, -1):
        print("|" * p + "+" + "-" * ((frme * 2) + lm - 2 * p) + "+" + "|" * p)
        
main()