import math
def main():
    a=eval(input("Enter the starting point N:\n"))
    b=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(a+1,b):
        num1=str(i)
        num2=num1[::-1]
        if num1==num2 and i!=1:
            count=0
            d=math.sqrt(i)
            d=round(d)
            a=2
            while a<=d:
                if i%a==0:
                    count+=1
                a+=1
            if count==0:
                print(i)
main()