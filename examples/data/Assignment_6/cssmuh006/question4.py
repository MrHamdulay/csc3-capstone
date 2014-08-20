marks=input("Enter a space-separated list of marks:\n").split(" ")
#variables to store the X's
v=""
w=""
x=""
y=""
z=""
for j in marks:
        #determining X's for each category        
        if eval(j)>=75:
                v=v+"X"
        if 70<=eval(j)<75:
                w=w+"X"
        if 60<=eval(j)<70:
                x=x+"X"
        if 50<=eval(j)<60:
                y=y+"X"
        if eval(j)<50:
                z=z+"X"
                
print("1 |",v,"\n","2+|",w,"\n","2-|",x,"\n","3 |",y,"\n","F |",z,"\n",sep="") #displaying output