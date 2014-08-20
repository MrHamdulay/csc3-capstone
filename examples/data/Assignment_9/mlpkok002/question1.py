import math
#open the filename:
filename=input("Enter the marks filename:\n") 
f=open(filename, "r")
lines=f.readlines()
f.close()

#calculate the sum of the marks:
Sum=0
for i in range(len(lines)):
    Position=lines[i].find(",")
    y=eval((lines[i][Position+1:]))
    Sum+=y
#calculate average    
average=Sum/len(lines)

#algorith to get 2 decimal places for the average 
Average=str(average)
position=Average.find(".")
if Average[position+1:]=="0":
    new_average=Average+"0"
else:
    new_average=round(average,2)

print("The average is:",new_average)


#calculate std dev:
a=0
for i in range(len(lines)): 
    POSITION=lines[i].find(",")
    y=eval((lines[i][POSITION+1:]))
    a+=(y-average)**2

sd=math.sqrt(a/len(lines))
SD=str(sd)

#algorith to get 2 decimal places for the std_dev
position2=SD.find(".")
if SD[position2+1:]=="0":
    new_SD=SD+"0"
else:
    new_SD=round(sd,2)

print("The std deviation is:",new_SD)

#calculate the cut_off (one std_dev below the mean)
cut_off=average-sd

dp_risk=[] 
for i in range(len(lines)):
    position_comma=lines[i].find(",")
    if eval((lines[i][position_comma+1:]))<cut_off: #get the names of students whose marks are below the cut_off
        position3=lines[i].find(",")
        dp_risk.append(lines[i][:position3])
        

DPR_list=" ".join(dp_risk) #convert the list of names of students whose marks are below the cut_off into a one string
s=DPR_list

if len(s)==0:
    print("")
else:
#recurse over the string, putting every name on a new line
    def new_line(s):
        position4=s.find(" ")
        if position4==-1:
            return s
        else:
            return s[:position4]+"\n"+new_line(s[position4+1:])
    print("List of students who need to see an advisor:\n"+new_line(s))


    



        
        
   
