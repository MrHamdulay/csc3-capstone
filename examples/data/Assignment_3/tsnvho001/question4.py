#Program to determine parlindromic primes between two numbers
#Tsanwani Vhonani
#20 March 2014

def palindromic_primes():
    x=eval(input("Enter the starting point N:\n"))
    y=eval(input("Enter the ending point M:\n"))
    x+=1
    print("The palindromic primes are:")
    for i in range(x,y):
        y=True
        if str(i)==str(i)[::-1]:
            if(i>=2):
                for a in range(2,i):
                    if i%a==0:
                        y=False
                        break
                if y:
                    print(i)
palindromic_primes()


    
    