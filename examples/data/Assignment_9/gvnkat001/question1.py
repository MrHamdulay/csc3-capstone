#Katlego Gaveni 12th May 2014
#programme that runs a file name containing names and student number - the programme determines the average,std deviation and a list of students who require assitance. 
import math

            

def marks(lines,names,mark):
    for i in range(len(lines)):
        x=""
        x+=lines[i]
        for j in range(len(x)):
            if x[j]==",":
                position=j
                names.append(x[0:position])
                mark.append(x[position+1:])
                
                
def average_std(mark,names,student_alert):

    x=0
    formatting = "{0:0.2f}"
    for i in range(len(mark)):
        x+=eval(mark[i])
     
    average1=(x/(len(mark)*100))*100
    
    
   
    total_marks=0
    
    for i in range(len(mark)):
        total_marks+= (eval(mark[i])- average1)**2
        
    std_deviation1=math.sqrt(total_marks/len(mark))
    std_deviation=formatting.format(std_deviation1)
    average=formatting.format(average1)
    
    for i in range(len(mark)):
        if eval(mark[i]) < (average1 - std_deviation1):
            student_alert.append(names[i])
            
    
    print("The average is:",average)
    print("The std deviation is:",std_deviation)
    
    
    if len(student_alert)>0:
        print("List of students who need to see an advisor:")
        for i in range(len(student_alert)):
            print(student_alert[i])
 
    else:
        return ""



def main():
    file=input("Enter the marks filename:\n")
    
    f=open(file,"r")
    
    lines = f.readlines ()
    f.close ()
     
    names=[]
    mark=[]
    student_alert=[]
    
    marks(lines,names,mark)
    average_std(mark,names,student_alert)

main()