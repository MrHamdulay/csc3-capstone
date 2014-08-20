""" A program to reformat a text file so that all lines are at most a given length """
""" Gadziraiushe Bangure """
""" 16 May, 2014 """


input_ = input("Enter the input filename:\n")   
output_ = input("Enter the output filename:\n") 
line_width = eval(input("Enter the line width:\n"))  


f=open(input_,"r")
f2=open(output_,"w")
string_input=f.read()                  

#create a list of strings
list_s = string_input.split("\n\n")  

parag="" # initialization as an empty string   

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