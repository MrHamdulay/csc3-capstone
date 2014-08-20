# 09/05/2014 
# SCHCH027
# Question1
import sys
sys.setrecursionlimit (40000)

start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))

# checks if the number in question is prime
def primeCheck2(num,digit):
      if num==1:
            return False
      else:          
            if num!=digit:
                  if num%digit!=0:
                        digit+=1
                        isPrime=primeCheck2(num,digit)
                        return isPrime
                  else:
                        return False
            else:
                  return True
#checks if the number in question is a palindrome
def palinCheck2(currentNumber,end,count):
    rev=reverse(str(currentNumber))
    tes=int(rev)
    if tes==currentNumber:
        return True
    else:
        return False
#reverses the number in question, used in palindrome checker
def reverse(string):
    if string=="":
        return string
    else:
        return reverse(string[1:])+string[0]
# check2 calls and controls other functions ( palindrome check, palindrome check)
def check2(currentNumber,end, count):
    if currentNumber!=end+1:
        
        tof=palinCheck2(currentNumber,end,count)
        
        if tof==True:
            digit=2
            isPrime=primeCheck2(currentNumber,digit)
            if isPrime==True:
                print(currentNumber)
            currentNumber+=1    
            check2(currentNumber,end, count)
        else:
            currentNumber+=1
            check2(currentNumber,end, count)
  
print("The palindromic primes are:")
check2(start,end,1)