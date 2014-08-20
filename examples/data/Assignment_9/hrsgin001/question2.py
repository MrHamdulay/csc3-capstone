#Question 2, Assignment 9
#Gina Horscroft
#10.05.2014

inp = input("Enter the input filename:\n")
out = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
#read the file
inputF = open(inp, "r")
s = inputF.read()
inputF.close()
arr = s.split("\n")
   
newarr = []
for i in range (len(arr)):
    st = arr[i]
    if st == '':#means used to be \n\
        st = "\n\n"
    newarr += st.split(" ")

count = 0
newstr = ""
for i in range(len(newarr)):
    temp = newarr[i]#temp word
    if newarr[i] == "\n\n":
        newstr += temp
        count = 0
    elif(count+len(temp) <=width ):
        newstr+=temp + " "
        count+=len(temp) + 1
    else:
        count = 0      
        newstr+="\n" + temp + " "
        count+=len(temp) + 1
    
#Write spaced line to file    
outputF = open(out, "w")
print(newstr, file = outputF)
outputF.close()
