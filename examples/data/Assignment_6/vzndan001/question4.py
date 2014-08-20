"""histrogram representing mark distribution
danica van der zandt
24 april 2014"""

#get input from user and split into list of individual marks
marks=input("Enter a space-separated list of marks:\n")
ind_marks=marks.split()
number_marks=len(ind_marks)

#catergorising each mark and adding to its counter
count=[0,0,0,0,0]
for x in ind_marks:
    x=int(x)
    if x < 50:
        count[0]+=1
        
    elif 50<=x<60:
        count[1]+=1
                
    elif 60<=x<70:
        count[2]+=1
            
    elif 70<=x<75:
        count[3]+=1
        
    elif 75<=x<=100:
        count[4]+=1
        
#to print our little histogram
print("1 |"+"X"*count[4]+"\n2+|"+"X"*count[3]+"\n2-|"+"X"*count[2]+"\n3 |"+"X"*count[1]+"\nF |"+"X"*count[0])
