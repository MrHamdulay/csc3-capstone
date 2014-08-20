#this program reformat the text to fit into a given space
#Hebert TEMA- TMXTHA006
#10 MAY 2014



def write_line(array,width,ans="", line=""):
    """this function returns the formatted data of the file read in one string"""
    if len(array):
        l=len(line)+len(array[0]) 
        if not array:
            ans+="\n"+line
        elif bool(l<width)==True:
            line+=" "+array[0]
            del array[0]
            return   write_line(array,width,ans,line)
        elif l>=width and array:
            ans+="\n"+line
            return write_line(array,width,ans, line="")
        else:
            ans+="\n"+line
    ans+="\n"+line
    return ans
    

#get the input from the user
file_r=input("Enter the input filename:\n")          #file containing data
file_w=input("Enter the output filename:\n")        #file with the output
width=eval(input("Enter the line width:\n"))                #space the text has to fit in

try:
    #read data
    data=''
    f_in=open(file_r, "r")
    data=f_in.read()
    f_in.close()
    
    #split read data into a list
    array=data.split("\n")
    string=" ".join(array)
    list_s=string.split(" ")
    ans=write_line(list_s,width)
    
    array2=ans.split("\n")
    
    #write the output file
    f_out=open(file_w, "w")
    for i in array2:
        print(i[1:], file=f_out)
    f_out.close()
    print("done")
except:
    print()
    
