"""Histogram form list
Roger Cox
24/04/2014"""
markslist=[]
marks=input("Enter a space-separated list of marks:\n")
markslist=marks.split(" ")
#print(markslist)
# empty lists
fail=[]
n1=[]
n21=[]
n22=[]
n3=[]
#sort appropriate mart to list
for mark in markslist: 
     
     if eval( mark)<50 :
          fail.append(mark)
          
     elif eval( mark)<60 :
          n3.append(mark)
          
     elif eval( mark)<70 :
               n22.append(mark)     
          
     elif eval( mark)<75 :
          n21.append(mark)  
          
     else :
          n1.append(mark)   
          
# printing the output          
print("1 |",len(n1)*"X",sep="")
print("2+|",len(n21)*"X",sep="")
print("2-|",len(n22)*"X",sep="")
print("3 |",len(n3)*"X",sep="")
print("F |",len(fail)*"X",sep="")

     
