#HLNSIB005 : Sibulele Hlongwane
height=eval(input("Enter the height of the triangle:\n"))
count=height
for i in range(height):
    print(' '*(count-1), ("*"*(2*(i+1)-1)), sep="")
    count=count-1
#2-->3
#3-->5  
#4-->7
#5-->9
#10-->17