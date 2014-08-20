#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     19-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    start = eval(input("Enter the starting point N: \n"))
    end = eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    for i in range(start+1,end):
        if str(i) == str(i)[::-1]:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i)

if __name__ == '__main__':
    main()
