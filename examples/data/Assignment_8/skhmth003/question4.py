#Program that prints palindromic primes 
#Gordon Skhosana
#8/05/2014

import math
import sys
sys.setrecursionlimit (30000)
array=[]

def prime(N,i):
    global array
    if N==1:
        prime(N+1,i)
    elif N==M+1:
        return ""
    elif N!=i and (N%i==0):
        i=2
        prime(N+1,i)
    else:
        if i>math.sqrt(N):
            array.append(N)
            i=2
            prime(N+1,i)
        else: prime(N,i+1)
    return (array)
def reverse(word):
    if len(word)==0:
        return ""
    else:
        return word[-1] + reverse(word[0:len(word)-1])
def manipulate_array(array):
    if array==[]:
        return ""
    else:
        word=str(array[0])
        reverse(word)
        if word==reverse(word):
            print(reverse(word))
            del array[0]
            manipulate_array(array)
        else:
            del array[0]
            manipulate_array(array)   
def main():
    global M
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    i=2
    prime(N,i)
    print("The palindromic primes are:")
    manipulate_array(array)
main()