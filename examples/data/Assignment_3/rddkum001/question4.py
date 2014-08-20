def palindrome(N,M):
    for i in range(N+1,M):
        if i<12:
            if str(i)==str(i)[::-1]:
                if i//2==1 and i%2==0:
                    print(i)
                elif i//3==1 and i%3==0:
                    print(i)
                elif i//5==1 and i%5==0:
                    print(i)
                elif i//7==1 and i%7==0:
                    print(i)
                elif i//11==1 and i%11==0:
                    print(i)
                else:
                    continue
        else:
            if i>12:
                if str(i)==str(i)[::-1]:
                    if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0 or i%13==0 or i%17==0 or i%19==0 or i%23==0 or i%29==0 or i%31==0 or i%37==0 or i%41==0 or i%43==0 or i%47==0 or i%53==0 or i%59==0 or i%61==0 or i%67==0 or i%71==0 or i%73==0 or i%79==0 or i%83==0 or i%89==0 or i%97==0 or i%101==0 or i%103==0 or i%107==0 or i%109==0:
                        continue
                    else:
                        print(i)
                else:
                    continue
if __name__=='__main__':
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input('Enter the ending point M:\n'))
    print("The palindromic primes are:\n",end='')
    palindrome(N,M)
        
            
            
            