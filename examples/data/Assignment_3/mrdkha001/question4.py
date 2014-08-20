#Find all palindromic primes between two integers supplied as input (start and end points are excluded).

#A palindrome number is a number that reads the same from the front and the back. Examples are: 212, 44, 9009, 4567654. To calculate whether a number is a palindrome or not, you can first reverse the number (using the % operator and a loop, or a String) and then check for equality.

#A prime number is one that is only divisible by 1 and itself. Examples are: 3, 11, 313.

#Some examples of palindromic primes are: 11, 191, 313

def Check_Prime(Z):
    Multiples = 0
    if Z == 2:
        print(Z)
    if Z % 2 == 0:
        Multiples = Multiples + 1 
    if 3.00 - (Z**0.5) == 0:
        Multiples = Multiples + 1
    if Z > 2:
        for i in range(3,int((Z**0.5) + 1),2):
            if Z%i == 0:
                Multiples = Multiples + 1
    if Multiples == 0:
        print(Z)
    
def Check_Palindrome(N, M):
    print("The palindromic primes are:")
    for i in range (int(N) + 1, int(M), 1):
        if str(i) == str(i)[::-1]:
            Check_Prime(i)
                
start = input("Enter the starting point N:\n")
end = input("Enter the ending point M:\n")

Check_Palindrome(start, end)