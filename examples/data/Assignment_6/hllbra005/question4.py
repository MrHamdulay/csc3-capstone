# Histogram of list of marks
# Brandon Hall (HLLBRA005)
# 25/04/2014

one, two_plus, two_minus, three, F = 0 , 0, 0 , 0, 0  # sets all of vairables to zero
                                                      # These variables track the number of 
                                                      # students in each category

print("Enter a space-separated list of marks:")

user_list = input()
python_list = user_list.split(" ")  # Splits the string up into a list
                                    # What is in each block of the list is determinded
                                    # by what is on the left and right of the space
                                    # i.e The split character

for i in range (len(python_list)):
    
    mark = int(python_list[i])    
       
    if(mark<50):
        
        F += 1
       
    elif(50 <= mark < 60):
      
        three += 1   
        
    elif(60 <= mark < 70):
      
        two_minus += 1
        
    elif(70 <= mark < 75):
              
        two_plus += 1

    elif(75 <= mark):
          
        one += 1    


# The code below prints the histogram by using the "counting" variables 

print("1 |" + ("X" * one))  
print("2+|" + ("X" * two_plus))        
print("2-|" + ("X" * two_minus ))        
print("3 |" + ("X" * three))        
print("F |" + ("X" * F))        