#Joy Arendse-Gorvalla
import sys
sys.setrecursionlimit (30000) #increases the amount of recursion that python will allow

def palindrome(start,end): #defining a function
    print("The palindromic numbers are:")
    

def main():
    start = eval(input("Enter the starting point N:\n")) #asks user for starting point input
    end = eval(input("Enter the ending point M:\n")) #ASKS USER FOR ENDING POINT INPUT      
    palindrome(start,end)

main()   

