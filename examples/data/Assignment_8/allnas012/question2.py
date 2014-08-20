def count(x):
    if x == x[len(x)-1]:   
        return 0
    elif x[0]==x[1]:
        if len(x)>2:
            return 1+count(x[2:])
        else:
            return 1+count(x[1:])
    else:       
        return count(x[1:])

if __name__ == "__main__":  
    y = input("Enter a message:\n")
    print("Number of pairs:",count(y))