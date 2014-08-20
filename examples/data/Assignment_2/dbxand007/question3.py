# Cherise Dube
# 13 March 2014
# Proram to work out the approximation of pi and calculate the area of a circle given a radius by a user


i=2**(.5)
answer_2 = 0
answer = (2/i)*2
while i<2:
    i=(2+i)**(.5)  
    answer_2 = (2/i)*answer
    answer= answer_2
          
       
            
answer_3 = round(answer,3)
print("Approximation of pi:", answer_3)
radius= eval(input("Enter the radius:\n"))
area= (radius**(2))*answer_2 
print ("Area:",round(area,3))  