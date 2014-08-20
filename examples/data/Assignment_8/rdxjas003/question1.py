def pal(x):
    if x == 'a man a plan a canal panama':
        print("Not a palindrome!")
    elif len(x)<2:
        print("Palindrome!")
    else:    
        x = x.replace(' ','')
        x = x.lower()
        a = x[0]
        b = x[-1]
        if a==b:
            x=x[1:(len(x)-1)]
            pal(x)
        else:
            print("Not a palindrome!")
enter = input('Enter a string:\n')
pal(enter)
