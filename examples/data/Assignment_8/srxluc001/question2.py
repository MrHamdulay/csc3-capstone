def Repeat(x):
    if len(x)<2:
        return 0
    elif x[0]==x[1]:
        return 1 + Repeat(x[2:])
    else:
        return Repeat(x[1:])
def main():
    Q=input("Enter a message:\n")
    print("Number of pairs:",Repeat(Q))
main()
          
#for question 2 i ma having problems with line 2 
#i am trying to get the code to check each and every word after the second one 
#to see if it is equal to the last one

#the sructure of the code is,i  chek to see if the lenght of a variable is o
#if it is it should return nothing
#if the lenght of is greater than 2 and the forst and second words are equale
#IT should return 1
#the problem is what reursuion to use if the lengh is greater than 2
#the code doesn't run that far
