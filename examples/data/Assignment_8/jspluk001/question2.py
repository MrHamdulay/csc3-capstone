'''Luke Joseph
2014-05-07
question 2 of assignment 8'''

# Function calculating number of pairs
def pairs(x):
    count=0
    if len(x)<2:
        return 0
    else:
        if x[0]==x[1]:
            return 1 + pairs(x[2:])
        else:
            return 0 + pairs(x[1:])

# Main function printing outputs
def main():
    x=input("Enter a message:\n")
    y=pairs(x)
    print("Number of pairs:",y)
        
main()