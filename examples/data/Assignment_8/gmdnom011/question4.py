# Program to find all palindromic primes in a given range
# Nomsa Gamedze
# 7 May 2014

import sys
sys.setrecursionlimit (30000)
import math

def reverse_word(word, word2):
    if len(word2) < len(word):
        x = len(word) - len(word2) - 1
        word2.append(word[x])
        reverse_word(word, word2)
        return word2

def check_equal(wordA, wordB, a):
    if wordA[a] == wordB[a]:
        b = len(wordA) - 1
        if a < b:
            a += 1
            check_equal(wordA, wordB, a)
            return True
    else:
        return False

def find_primes(x, primes, a, y): # x is the starting point, y is the ending point
            x = x
            primes = primes
            a = a
            y = y
            if x < y:
                        if x == 2 or x == 3:
                                    primes.append(x)
                                    x += 1
                                    find_primes(x, primes, 2, y)
                        elif x == 1:
                                    x += 1
                                    find_primes(x, primes, 2, y)
                        if a <= int(math.sqrt(x)):          
                                    if x % a == 0:
                                                x += 1
                                                find_primes(x, primes, 2, y)
                                    if x % a != 0:
                                                a += 1
                                                find_primes(x, primes, a, y)
                                    if a >= int(math.sqrt(x)):
                                                if x % a != 0:
                                                            primes.append(x)
                                                            x +=1
                                                            find_primes(x, primes, 2, y)
                                                if x % a == 0:
                                                            x +=1
                                                            find_primes(x, primes, 2, y)
            primes = set(primes)
            primes = list(primes)
            return primes                                                

    
def is_palindrome(word):
    word2 = []
    word = list(word)
    word3 = reverse_word(word, word2)
    answer = check_equal(word3, word, 0)
    return answer

def keep_palindromes(many_primes, i, result):
    many_primes = many_primes
    i = i
    result = result
    prime = str(many_primes[i])
    if i < (len(many_primes) - 1):
        if ispalindrome(prime):
            i += 1
            result.append(prime)
            keep_palindromes(many_primes, i, result)
        else:
            i += 1
            keep_palindromes(many_primes, i, result)
    return result
            
        
       
def main():
    start_pt = eval(input("Enter the starting point N:"'\n'))
    end_pt = eval(input("Enter the ending point M:"'\n'))
    print("The palindromic primes are:")
    x = start_pt + 1
    primes = find_primes(x, [], 2, end_pt)
    pal_primes = keep_palindromes(primes, 0, [])
    pal_prime_list = '\n'.join(pal_primes)
    print(pal_prime_list)

# main()