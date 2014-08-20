print("Enter a space-separated list of marks:")

list_1=[]   #init list_1

input_a=input()  #a to input_a  
input_a=input_a.split()

for i in input_a:
        
        list_1.append(i)
        
list_1.sort()

grade=[] #list of grades

for i in list_1:
        
        int_b=int(i)  #an int_b
        
        if int_b<50:
                
                i="F"
                
        elif int_b<60:
                
                i="3"
                
        elif int_b<70:
                
                i="2-"
                
        elif int_b<75:
                
                i="2+"
        else:
                i="1"
                
        grade.append(i)
        
M=[]   
N=["1","2+","2-","3","F"]   
for k in range(5) :   
        
        w=N[k]   
        v=grade.count(w)  
        M.append(v)
    

for l in range(5):    #i to l
        
        z=N[l]
        form_z ="{0:<2}".format(z)   #zz to form_z
        out_put=M[l]
        print(form_z,"|","X"*out_put,sep="")