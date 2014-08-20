N=int(input("Enter the starting point N:\n"))
M=int(input("Enter the ending point M:\n"))
list2=[]
def palindrome(list):
    print("The palindromic primes are:")
    for i in range(len(list)):
        list[i]=str(list[i])
        i_rev=list[i][::-1]
        if list[i]==i_rev:
            list2.append(list[i])
            print(list[i])
        else: continue
    #print("The palindromic primes are:\n",list2)


def primes(N,M):
    list_primes=[]
    for i in range(N+1,M):
        p = 0
        for a in range (2,i):
            if i %a==0:
                break
            else:
                #list_primes.append(i)
                p += 1
        if p == i - 2:
            list_primes.append(i)
    #print(list_primes)
    return list_primes
#primes(N,M)
palindrome(primes(N,M))