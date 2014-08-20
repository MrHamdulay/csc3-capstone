def a(num,star):
    gap=(num//1)-1
    for i in range(1,num*2,2):
        print(' '*gap,end='') 
        print(star*(i))
        gap=gap-1 
num=eval(input("Enter the height of the triangle:\n"))
star='*'
a(num,star)
