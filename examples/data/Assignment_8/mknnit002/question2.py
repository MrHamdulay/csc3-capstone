#mknnit002
#question 2 ass 8
#number of pairs in a string

def pairs (string):
    if len(string)<=1:
        return 0
    elif string[0]!=string[1]:
        return pairs (string[1:])
    else:
        return 1+pairs(string[2:])
    
def main():
    x=input("Enter a message:\n")
    print("Number of pairs:",pairs(x))
    
main()

    