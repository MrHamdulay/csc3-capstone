""" Assignment 8 
Question 4 - palindrome prime
THNSIK001"""
import sys
sys.setrecursionlimit (30000)

def rev(word):
    #reverses word
    if word =="":
        return word
    return rev(word[1:]) + word[0]

def div(st,divider):
    #finds number of dividers
    if divider ==1:
        return 1
    if divider ==0:
        return 0
    elif st%divider==0:
        return 1 + div(st,divider-1)
    else:
        return div(st,divider-1)

def prpal(st,en):
    if st == en and str(st) == rev(str(st)) and div(st,st-1)==1:
        print(st)
    elif st == en:
        return ""
    elif str(st) == rev(str(st)) and div(st,st-1)==1:
        print(st)
        return prpal(st+1,en)
    else:
        return prpal(st+1,en)

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
prpal(start,end)