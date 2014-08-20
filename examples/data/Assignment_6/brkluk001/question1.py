'''Program to right allign names
23 April 2014
Luke Barker'''


list_strings =[]   #empty list
string = input('Enter strings (end with DONE): \n')
while not string == 'DONE':    #keep adding input until DONE is entered
    list_strings.append(string)  #adds string to a list
    string = input()

long_string = 0    #make a variable to keep track of the longest string    
for i in list_strings:    #iterate through list to find longest string
    if len(i) > long_string:
        long_string = len(i)
print()
print("Right-aligned list:")
for i in list_strings:
    format_string = ("{0:>"+str(long_string)+"}").format(i)  #format as per sample I/O
    print(format_string)
    
    
    