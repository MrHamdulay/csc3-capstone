starting_point=eval(input("Enter the starting point N:\n"))+1
end_point=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(starting_point,end_point):
    forward=str(i)
    reverse=forward[::-1]
    if reverse==forward:
        divisor=0
        for j in range(1,i+1): 
            if i%j==0: divisor+=1
        if divisor==2: print(i)