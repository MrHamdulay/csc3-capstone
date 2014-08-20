"""PRIYANKA GOBERDHAN
15/05/14
ASSIGN 9 - Q2"""

input_file = input("Enter the input filename:\n")
f_i = open(input_file,"r")

output_file = input("Enter the output filename:\n")
f_o = open(output_file,"w")
t = f_i.read() #Read Text

position = 0
counter = -1

width = eval(input("Enter the line width:\n"))

for i in range(len(t)):
    if(i==len(t)-1):
            x = []
            x.append(t[counter+1])
            for j in range(counter+2,i):
                if(t[j] != '\n'):
                    x.append(t[j])
                else:
                    x.append(" ")
            x.append(t[i])      
            for j in x:
                print(j,end = '',file=f_o)
                
    elif(t[i] == "\n" and t[i+1] == "\n"):
        x = []
        x.append(t[counter+1])
        for j in range(counter+2,i):
            if(t[j] != '\n'):
                x.append(t[j])
            else:
                x.append(" ")
        x.append(t[i])
        for j in x:
            print(j,end = '',file = f_o)
        print("",file = f_o)        
        
        counter = i+1     
    
    elif(i == counter+width and t[i+1] == " "):
        x = []
        x.append(t[counter+1])
        for j in range(counter+2,i):
            if(t[j] != '\n'):
                x.append(t[j])
            else:
                x.append(" ")
        x.append(t[i])
        for j in x:
            print(j,end = '',file = f_o)
        print("",file = f_o)        
        
        counter = i+1
    
    elif(i == counter + width and t[i+1] != " "):       
        for j in range(i,counter,-1):
            if(t[j] == " " or t[j] == "\n"):
                position = j
                break
        x = []
        x.append(t[counter+1])
        for j in range(counter+2,position-1):
            if(t[j] != '\n'):
                x.append(t[j])
            else:
                x.append(" ")
        x.append(t[position-1])        
        for j in x:
            print(j,end = '',file=f_o)
        print("",file = f_o)
        counter = position

#Close files
f_i.close()
f_o.close()