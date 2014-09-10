# [allnas012]
# [question1.py]

#Nasiha Ally
#ALLNAS012
#May 2014




def pal(string):
   if (string):
      if (string[0] == string[-1]):
         result =pal(string[1:-1])

         if result:
            return True
   else:
      return True
   return False

if __name__ == "__main__":
   x = input("Enter a string:\n")
   result = pal( x )

   if not result:


      print("Not a palindrome!")
   else:
      print("Palindrome!")



# [allnas012]
# [question3.py]

def encode_rec(x):
    if x[0]==" ":
        return " "+encode_rec(x[1:])
    elif x[0]==x[len(x)-1]:
        if x[0].islower():
            if x[0]=="z":
                return "a"
            else:
                return chr(ord(x[0])+1)
        else:
            return x[0]
    elif x[0].islower():
        if x[0]=="z":
            return "a"+encode_rec(x[1:])
        else:
            return chr(ord(x[0])+1)+encode_rec(x[1:])
    elif x[0].isupper():
        return x[0]+encode_rec(x[1:])
    else:
        return encode_rec(x[1:])

if __name__ == "__main__":
    ans = input("Enter a message:\n")
    print("Encrypted message:")
    print(encode_rec(ans))

# [allnas012]
# [question4.py]



import sys
import math
sys.setrecursionlimit (30000)


def rev(w):
    w = str(w)
    if w == "":
        return w
    else:
        return (rev(w[1:])+w[0])


def prime_num(n,divide=2):
    if n==1:
        return False
    elif divide>math.sqrt(n):
        return True


    elif (n%divide)==0:
        return False
    else:
        divide+=1
        return prime_num(n,divide)

def pal(s, e):
    if s!=e:
        if s==int(rev(s)) and prime_num(s):
            return str(s) + "\n" + pal(s+1,e)
        else:
            return pal(s+1,e)

    else:
        if prime_num(s) and s==int(rev(s)):
            return str(s)
        else:
            return ""

if __name__ == "__main__":

    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    print(pal(N,M))

# [allnas012]
# [question2.py]



def count(x):
    if x == x[len(x)-1]:
        return 0
    elif x[0]==x[1]:
        if len(x)>2:
            return 1+count(x[2:])
        else:
            return 1+count(x[1:])
    else:
        return count(x[1:])

if __name__ == "__main__":
    y = input("Enter a message:\n")
    print("Number of pairs:",count(y))

