""" recursive function to count the number of pairs of repeated characters in a string
Ross Eyre
05/05/2014"""

def main():
    msg = input("Enter a message:\n")
    n = pairs(msg)
    print("Number of pairs:", n)

# count pairs of characters 
def pairs(string):
    if(len(string)==0): #if string contains nothing, we are done
        return 0
    elif(string[0:1]==string[1:2]): #if char equals char next to it, return 1 and move on, cutting off both characters to prevent overlap
        return 1 + pairs(string[2::])
    else:  #
        return pairs(string[1::])
    
main()