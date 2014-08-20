"""Sumayah Goolam Rassool
Program to calculate and store standard deviation
11 May 2014"""

#------------------------------------------------imports the math class to use square root function----------------------------
import math

def main():
    
    try:

#-----------------------------------------------Asks user for file name used to store the marks-------------------------------    
        filename=input("Enter the marks filename:\n")
    
        infile=open(filename,"r")
#----------------------------------------------Creates array to store marks and array to store names    
        array=[]
        names=[]
    
#--------------------------------------------Goes through each line in file and splits the name and surname using "," as separator    
        for line in infile:
        
            name,mark=line.split(",")
#-------------------------------------------adds names and marks to respective arrays
            array.append(int(mark))
            names.append(name)
        
        sum=0

#------------------------------------------runs through array containing marks and finds the sum
    
        for i in range (len(array)):
            sum+=array[i]
        
#-----------------------------------------Calculates the average using the sum
        avg=round(sum/(len(array)),2)
    
    
        step2=0
    
#----------------------------------------runs through array to calculate standard deviation
        for j in range (len(array)):
       
            step1=(array[j]-avg)*(array[j]-avg)
        
            step2+=step1
        
        step3=step2/(len(array))
    
        stnd=math.sqrt(step3)
#--------------------------------------minimun mark represents average - standard deviation    
        min_mark=avg-stnd
        
        
        
        print("The average is: {0:0.2f}".format(avg))
        print("The std deviation is: {0:0.2f}".format(stnd))
        
        
            
        
        student=[]
            
        #----------------------------------------checks for students with less than the minimun mark and prints their names
            
        for k in range (len(array)):
                
            if array[k]<min_mark:
                student.append((names[k]))
        
        if student:
            print("List of students who need to see an advisor:")
            
            for l in range (len(student)):
                print(student[l])
                
    except IOError as errno:
        
        print("could not read file")
        print("Error number:",errno)
        
    
        
                    
              
main()