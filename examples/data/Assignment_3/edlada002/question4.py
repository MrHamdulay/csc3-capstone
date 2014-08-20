start = eval(input("Enter the starting point N:\n"))
end =eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
  
  
  
  

  
    
def isPalindrome(number):
  
    if (str(i) == str(i)[::-1]):
          return True



  
def isPrime(num):
    prime = True

    if num > 1:
   
        for i in range(2,num):
            if (num % i) == 0:
                prime = False

        return prime
for i in range (start+1,end):
    if isPalindrome(i) and isPrime(i):
        print(i)
  
  
