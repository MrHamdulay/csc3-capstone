#The program prints out an isoceles triangle with height given
#Student no.:TMXTHA006
#Name: TEMA, Thabo Hebert
#Date: 20 March 2014

h = eval(input("Enter the height of the triangle:\n"))
p = 1
q = h-1
for i in range(h):
    print(" "*q, "*"*p, sep="")
    q-=1
    p+=2