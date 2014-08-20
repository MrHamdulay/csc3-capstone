#Assignment 8 - Question 2
#Counts number of pairs of repeated characters 
#Aidan de Nobrega
#05/05/2014

def countpairs(s): 
    if len(s) > 1: #pair, by definition, requires at least two characters
        if s[0] == s[1]: #if first two letters are the same
            #increments and invokes function on everything after that pair
            return 1 + countpairs(s[2:]) 
        else: 
            return countpairs(s[1:]) #else, just moves onto next letter in string
    else:
        return 0 #doesn't increment and ends function
    
def main():
    string = input("Enter a message:\n")
    pairs = countpairs(string) #fetches the incremented value from countpairs(string)
    print("Number of pairs:", pairs)

main()
        