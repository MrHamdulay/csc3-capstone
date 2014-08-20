#Question 2, Assignment 3
#Tejasvin Bagirathi

h = eval(input("Enter the height of the triangle:\n"))


for i in range(1,h+1):
    string1 = str(2*h)
    print(('{0:^' + string1 + '}').format('*'*(2*i - 1)))
    
          