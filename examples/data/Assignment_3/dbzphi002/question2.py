#Thembekile Dubazana
#19 March 2013
#Assignment 3 Q2

h=eval(input('Enter the height of the triangle:\n'))
gap= h-1
for i in range(1,h*2,2):
    print(gap*' ','*'*i, sep="")
    gap=gap-1
    
        