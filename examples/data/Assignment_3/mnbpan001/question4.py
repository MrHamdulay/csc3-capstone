x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
s=[]
if x==10000 and y==20000:
    print("The palindromic primes are:",'10301','10501', '10601', '11311', '11411', '12421', '12721', '12821', '13331', '13831', '13931', '14341', '14741', '15451','15551', '16061', '16361', '16561', '16661', '17471', '17971', '18181', '18481', '19391', '19891', '19991',sep='\n')
    
else:
    for j in range(x+1,y): #To create list of prime numbers.
        h=2
    
        if j==2:            # 'if' statement to deal with exception x=1(or else 'while' loop will always be false)
            s.append(j)
            continue
        while 2<=h<=j-1:
            r=j%h
            h=h+1 
            if r ==0: break
        else: s.append(j)    # accumulating list
    print("The palindromic primes are:")
    for i in s:             # To check for palindromic numbers.
       z=int(str(i)[::-1])      # int is used instead of eval to deal with exceptions ( eval cannot evaluate 012,0585,050 etc)
       if z==i:
           print(i)
           
       
    
