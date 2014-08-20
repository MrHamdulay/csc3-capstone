i = input("Enter the input filename:\n")   
o = input("Enter the output filename:\n") 
line_width = eval(input("Enter the line width:\n"))  


f=open(i,"r")
f2=open(o,"w")
string_input=f.read()                  

#creating  a list 
list_s = string_input.split("\n\n")  

parag="" 

for i in range(len(list_s)):
    string=list_s[i].replace("\n"," ")
    
    def lines(w):  
        if len(w)<=line_width:
            return w  
        else:
            x=1   
            line = w[:line_width]  
            z = w[line_width]  
             
            while z != " ":  
                line = w[:line_width-x]   
                z = w[line_width-x]  
                line_width-x  
                x+=1      
        return line+"\n"+lines(w[line_width-x+1:]).lstrip(" ")          
    parag+=lines(string)+"\n"+"\n"


print(parag,file=f2)
f.close()
f2.close()