#Amitha Doodnath - DDNAMI001
#08/05/2014
#Programme to find palindromic primes


import sys
sys.setrecursionlimit (30000)


def palindrome(word):
   
    if word == '':
        return True
    else:
        if word[0] == word[len(word)-1]:
            return palindrome(word[1:len(word)-1])
        else:
            return False
count=2      

def check_prime(num):
    global count
    if(num<2):
        return False
    else:
        if(num==4):
            return False
        if(num==3):
            return True        
        if(num==2):
            return True
        else:
            if count==(num//2):
                return True
            else: 
                if(num%count==0):
                    return False
                else:
                    count=count+1
                    return check_prime(num)
                                                             
def find(a,b):
    global count
    count=2
    if a == b:
        if palindrome(str(a)):
            if check_prime(a):
                print(a)        
        return True
    else:
        if palindrome(str(a)):
            if check_prime(a):
                print(a)
        a=a+1
        find(a,b)
    
def main():
    a=eval(input("Enter the starting point N:\n"))
    b=eval(input("Enter the ending point M:\n")) 
    print("The palindromic primes are:")
    find(a,b)                                

main()