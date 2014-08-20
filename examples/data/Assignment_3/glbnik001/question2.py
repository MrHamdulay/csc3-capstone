def a():
    h=eval(input("Enter the height of the triangle:\n"))
    space=h-1 
    counter=1
    for i in range(0,h):
        print(' '*space,end='')
        print("*"*counter)
        space=space-1
        counter=(counter+2)
a()