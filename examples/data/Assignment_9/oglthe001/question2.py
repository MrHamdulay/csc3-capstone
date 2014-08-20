file_input=input('Enter the input filename:\n')
file_output=input('Enter the output filename:\n')

#reading from file input
f1 = open (file_input, 'r')
string = ""
while 1:
    line = f1.readline()
    if not line:break
    string += line
f1.close()

print(string)
print(len(string))

given_length = eval(input('Enter the line width:\n'))

#reformatting the file input into a new file
f2 = open (file_output, 'w')
if len(string) <= given_length:
    f2.write(string[0:])
elif given_length < len(string) <= (given_length*2):
    f2.write(string[0:given_length],'\n',string[given_length:])
elif (given_length*2) < len(string) <= (given_length*3):
    f2.write(string[0:given_length],'\n',string[given_length:(given_length*2)],'\n',string[(given_length*2):])
f2.close ()