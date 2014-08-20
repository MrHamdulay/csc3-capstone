#SandyCris Mahlangu
#MHLSAN022
#QUESTION 4, THIS WAS HARD
a=eval(input('Enter the starting point N:\n'))
b=eval(input('Enter the ending point M:\n'))
def palipali(a,b):
        """This has got to be one of the most annoying programs ever"""
        a += 1
        
        for i in range(a,b):
                y = True
                if(str(i) == str(i)[::-1]):
                        if(i>=2):
                                for a in range(2,i):
                                        if(i%a==0):
                                                y = False
                                                break
                                       
                                if y:
                                                
                                        print(i)
print('The palindromic primes are:')
palipali(a,b)
