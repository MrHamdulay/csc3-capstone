"""Name: Sibulele Hlongwane
Date: 20 April 2014
Program: Calculate the dot, and the magnitude of vectors"""
#Prompts user to enter Vector A and B
A= input("Enter vector A:\n")
B= input("Enter vector B:\n")

#Splits string entered by user into a list
a= A.split(" ")
b= B.split(" ")
x=[]#Sum
#Initialises Magnitude of the Vectors to 0
VectorAMag=0
VectorBMag=0
VectorDot=0
count=-1
for c in a:
    count=count+1
    #Adds the vectors
    VectorSum= int(b[count])+ int(c)
    #Determines the dot product of the vectors
    VectorDotSum= int(b[count])*int(c) 
    VectorDot=VectorDot+VectorDotSum
    #Determines the magnitude of Vector A
    VectorAMag= VectorAMag+ int(c)**2
    #Determines the magnitude of Vector B
    VectorBMag= VectorBMag+ int(b[count])**2
    #adds sum of vector compenents into a list
    x.append(VectorSum)
  

"""prints the output, being the vector sum of vector a and b
the dot product of Vector A and Vector B
the magnitude of Vector A and Vector B invidiually,
with a format funtion, to display vector Magnitudes in two decimal places"""
print("A+B = "+ str(x) + "\n" + "A.B = "+ str(VectorDot)+ "\n"+"|A| = " +str("%0.2f"%((VectorAMag)**(1/2)))+ "\n"+ "|B| = "
            + str("%.2f" %((VectorBMag)**(1/2))))
