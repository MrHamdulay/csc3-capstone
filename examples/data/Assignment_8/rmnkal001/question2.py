#Kalind Ramnarayan
#number of pairs of repeated charters in a string.
#May 2014

def countpairs(string,number):
    if len(string)<2:                  # to check if string has one letter or none
        return print("Number of pairs:",number)

    elif string[0]==string[1]:
        number=number+1
        return countpairs(string[2:],number)# checks for pairs in every two charaters
    
    else:
        return countpairs(string[2:],number)#moves to the next two charaters
string=input("Enter a message:\n")
countpairs(string,0)




