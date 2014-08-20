# program that uses a recursive function to count the number of pairs repeated in a string
# khadeejah omar
# 4 may 2014

count = 0

def pair_counter(string) :
    global count
    
    # base case
    if string == "" or len(string) == 1 :
        print("Number of pairs:", count)
        
    # recursive step
    else:
        if string[0] == string[1] : # if the first two letters is a pair,  remove first two letters and do recursive step again
            count += 1
            return (pair_counter(string[2:]))
        else : # if the first two letters aren't a pair, remove the first letter and do recursive step again
            return (pair_counter(string[1:]))
    
def main() :
    string = input("Enter a message: \n")
    return(pair_counter(string))
    
main()