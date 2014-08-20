#Azhar Aboobaker
#ABBAZH001
#07/05/2014

message = input("Enter a message:\n")
def countpairs(x):
    pairs=0
    if len(x)<2:
        return pairs 
    else:
        if x[0]==x[1]:
            pairs=pairs+1
            return pairs+countpairs(x[2:])
        else:
            return pairs+countpairs(x[1:])

print("Number of pairs:",countpairs(message))
