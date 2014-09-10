# [sngsoh004]
# [question1.py]

#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 1


def inverse(string): #function to reverse the input
    if string=="":
        return string #empty string
    else:
        return (inverse(string[1:])+string[0]) #using recursion to keep putting the first letter to the end of the word, returns the original word completely reversed

word = input("Enter a string:\n")
if word==inverse(word): #if it is a palindrome


    print("Palindrome!")
else:
    print("Not a palindrome!")

# [sngsoh004]
# [question3.py]

#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 3

def encryption(string):
    if string[0]==" ":
        return " "+encryption(string[1:]) #if there is a space

    elif (string[0]==string[len(string)-1]): #If it is the last character

        if string[0].islower(): #only encrypt if its a lower case character
            if string[0]=="z": #changing z's to a's
                return "a"
            else:
                return chr(ord(string[0])+1)
        else:
            return string[0]

    elif string[0].islower(): #encrypting when it is not the last character

        if string[0]=="z":
            return "a"+encryption(string[1:])

        else:
            return chr(ord(string[0])+1)+encryption(string[1:])

    elif string[0].isupper(): #do not encrypt the character if it is upper case
        return string[0]+encryption(string[1:])

    else:
        return encryption(string[1:])

message = input("Enter a message:\n")
print("Encrypted message:\n"+encryption(message))

# [sngsoh004]
# [question4.py]

#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 4




import sys
import math
sys.setrecursionlimit (30000)


def inverse(number): #function to reverse the input
    string=str(number)
    if string=="":
        return string #empty string
    else:
        return (inverse(string[1:])+string[0]) #using recursion to keep putting the first letter to the end of the word, returns the original word completely reversed



def isPrime(n, divisor=2):
    if n==1: #1 is not a prime number
        return False

    else:
        if divisor>math.sqrt(n): #if the divisor is greater than half the number
            return True



        if n%divisor==0: #if it is completely divisable by the divisor
            return False

        else:
            divisor+=1
            return isPrime(n,divisor)


def mainFunction(start, end):
    if(start!=end):

        if int(inverse(start))==start: #if the number is a palindrome

            if isPrime(start): #if the palindrome is a prime
                return str(start) + "\n"+ str(mainFunction(start+1,end))

            else:
                return mainFunction(start+1,end)

        else:
            return mainFunction(start+1,end)

    else:
        if int(inverse(start))==start:
            if isPrime(start):
                return start
        else:
            return ""


number1 = eval(input("Enter the starting point N:\n"))
number2 = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:\n"+str(mainFunction(number1,number2)))

# [sngsoh004]
# [question2.py]

#Soham Hanuman Singh
#SNGSOH004
#Assignment 8
#Question 2



def countPairs(string): #function to count the number of pairs of a single letter
    if string==string[len(string)-1]:
        return 0 #if there is only one character left of the string

    elif string[0]==string[1]:
        if len(string)>2:
            return 1+countPairs(string[2:]) #incrementing the counter of consecutive letters then continuing to recurse through the word
        else:
            return 1+countPairs(string[1:])
    else:
        return countPairs(string[1:])

stringInput = input("Enter a message:\n") #asking for a string to be input

print("Number of pairs:",str(countPairs(stringInput))) #calling the
