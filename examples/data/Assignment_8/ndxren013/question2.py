"""reneshan naidoo
ndxren013
7 may 2014"""

def countpairs(message,x):
    if len(message)==0 or len(message)==1:# to check if string has length 1 or 0
        return print("Number of pairs:",x)

    elif message[0]==message[1]:
        x+=1
        return countpairs(message[2:],x)# checks for pairs in every 2 charater intervals
    else:
        return countpairs(message[2:],x)#moves to the next 2 charaters

def main():
    
    message=input("Enter a message:\n")#getting user input
    countpairs(message,0)

main()




