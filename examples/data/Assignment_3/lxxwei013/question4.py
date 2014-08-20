def palindromeprime():
    x=eval(input("Enter the starting point N:\n"))
    y=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")    
   
    for i in range(x+1,y):
        if(str(i) == str(i)[::-1]):
            count = i
            count2 = 0
            for j in range(count):
                number = count%(j + 1)
                if number == 0:
                    count2 = count2 + 1
            if count2 == 2:
                print(count)    
palindromeprime()