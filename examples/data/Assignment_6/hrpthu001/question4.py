"""program to create a histogram of marks
thushar hariparsad
22 april 2014"""

marks=input("Enter a space-separated list of marks:\n")

listofmarks=marks.split(" ")  #split list on basis of spaces

first=""                                                   
second_plus=""                                              
second_minus=""                                            
third=""                                                    
fail=""           

for i in listofmarks:   
    m=eval(i)
    if m>=75:
        first+="X" #create bar
    elif m>=70:
        second_plus+="X" 
    elif m>=60:
        second_minus+="X" 
    elif m>=50:
        third+="X" 
    else:
        fail+="X" 

print("1 |"+first)                                
print("2+|"+second_plus)                                    
print("2-|"+second_minus)                                   
print("3 |"+third)                                          
print("F |"+fail)                                           