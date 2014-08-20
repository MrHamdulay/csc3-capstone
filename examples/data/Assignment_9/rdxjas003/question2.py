#connect to text file
filename = input('Enter the input filename:\n')
file = open(filename,'r')

filename2 = input('Enter the output filename:\n')


width = eval(input('Enter the line width:\n'))

#store each word in list
charcount = 0
for line in file:
    x = line
    print(x)
    file2 = open(filename2,'w')
    file2.write(x) 
    
# Your program should store a single row of the triangle and calculate each    
#close access to file
file.close
file2.close