"""Assignment 9 Question 2
danson masuka 
14 May 2014"""

inpName = input("Enter the input filename:\n") #input filename        
afile=open(inpName,"r")  #open file                        
cont=[]                                             
for line in afile:                                     
    cont.append(line)                               
afile.close()   #close file



new_file=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

for line in range(len(cont)):
    if cont[line]=="\n":
        pass
    elif cont[line][-1:]=="\n":
        cont[line]=cont[line][:-1]
con = []
for line in range(len(cont)):  #loop
    cont[line]=cont[line].split(" ") 
    for word in range(len(cont[line])):  # iterate over word in e line
        con.append(cont[line][word])            

output_file=open(new_file,"w")    #write to new file
line=""  # create line variable


while True:
    try:
        if con[0]=="\n":  #if line is empty
            line=line+con[0]   
            print(line,file=output_file)  
            con.remove(con[0])
            line=""
        elif line=="":
            line = con[0]
            con.remove(con[0]) 
        elif len(line+" "+con[0])<=width:           
            line=line+" "+con[0]                    
            con.remove(con[0])                  
        else:
            print(line,file=output_file)                
            line=""    
    except:  #for errors
        print(line,file=output_file)
        output_file.close()
        break