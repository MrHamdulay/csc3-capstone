#Gillian Wachira
#09 May 2014


def reverseA(y):
   
    if len(y)==1:
        return 0
    elif y[0]==y[1]:
        if y[0]==y[2]:
            return (0 + reverseA(y[1:]))
        else:
            return (1 + reverseA(y[1:]))
    else:
        return (0 + reverseA(y[1:]))

    
def main(): 
    y=input("Enter a message:\n")             
    print ("Number of pairs:",reverseA(y))
main()