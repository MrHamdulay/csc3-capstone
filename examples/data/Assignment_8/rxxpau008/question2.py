#Count the number of pairs of letters using recursion
#Paul Roux - RXXPAU008
#08 May 2014

def check_pairs(string, count):
    """Looks for pairs of characters in a string using recursion by comparing
    characters and removing the appropriate number of characters for each 
    iteraation."""
    if len(string)>=2:
        if string[0]==string[1]:
            count+=1
            check_pairs(string[2:],count)
        else:
            check_pairs(string[1:],count)
    
    else:
        print("Number of pairs:",count)
    
check_pairs(input("Enter a message:\n"),0)