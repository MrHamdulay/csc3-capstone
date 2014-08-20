#Tato Moaki MKXTAT001
#Program to determine palindrome primes between two intervals
#question4 Assignment4
def main():
    var1 = eval(input("Enter the starting point N:\n"))
    var2 = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    if (var1 == 1):
        print("2")
        var1 += 1
    var1 += 1
    
    for l in range(var1,var2):
        l = str(l)
        if(l[::-1] == l):
            l = int(l)
            for k in range(2,l):
                if(l % k == 0):
                    break
            if(l % k != 0):
                print(l)
main()
                
                