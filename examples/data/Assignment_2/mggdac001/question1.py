def leap():
    x=eval(input('Enter a year:\n'))
    y= x/400
    #print(y)
    if (x%400==0):
        print(x,'is a leap year.')
    elif (x%4==0 and x%10!=0):
        print(x,'is a leap year.')
    else:
        print(x,'is not a leap year.')
    

    
    
leap()
          