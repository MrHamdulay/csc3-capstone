"""vector calculations
 Alexander Whiting
 23 April 2014"""
import math

def aplusb (a,b): #returns the sum of the vectors as a string in vector format
    AB = "["+str(int(vector_a[0])+int(vector_b[0]))+", "+str(int(vector_a[1])+int(vector_b[1]))+", "+str(int(vector_a[2])+int(vector_b[2]))+"]" # converts each part of the vector to an int and adds them
    return AB

def adotb (a,b): #returns the dot product
    answer = int(a[0])*int(b[0]) + int(a[1])*int(b[1]) + int(a[2])*int(b[2])
    return answer

def magnitude (vec): # returns the magnitude of the vector
    mag = math.sqrt((int(vec[0])**2)+(int(vec[1])**2)+(int(vec[2])**2))
    return mag 
 
 
vector_a = input("Enter vector A:\n").split(" ")
vector_b = input("Enter vector B:\n").split(" ")
"""gets vector inputs"""
print("A+B = "+ aplusb(vector_a,vector_b))
print("A.B = "+str(adotb(vector_a,vector_b)))
print("|A| = "+"%.2f" % magnitude(vector_a))
print("|B| = "+"%.2f" % magnitude(vector_b))



