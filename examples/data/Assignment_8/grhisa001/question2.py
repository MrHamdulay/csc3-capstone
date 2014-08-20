""" Bella Gorham 
pairs checkefr
06/05/14"""

def pairs(string):
    # if not long enough to be a pair 
    if len(string) == 1 or len(string) == 0:
        return 0
    
    # if beg and beg +1 are equal test again on next twp
    if string[0] == string[1]:
        
        return 1 + pairs(string[2:])
    
    else:
        return pairs(string[1:])
    
# function to get input   
def main():
    message = input("Enter a message:\n")
    print("Number of pairs:", pairs(message))
main()