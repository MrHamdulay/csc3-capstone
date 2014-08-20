"""This program prints out a ist of strings aligned whith the longest string
Hebert Tema
21-04-2014"""


#create an empty list
string_list=[]

#create a function with a sintinel loop
def list_str(string):
    string=string
    global string_list
    while string!="DONE":
        string_list.append(string)
        string=input()
    return string_list

if __name__=="__main__":    
    #prompt the user to enter the strings with the sintinel "DONE"
    string=input("Enter strings (end with DONE):\n")
    list_str(string)
        
    #find the length the longest string
    length=0
    for i in string_list:
        if len(i)>length:
            length=len(i)
        
    #format the ountput string
    format_string="{0:>"+str(length)+"}"
    
    #print out the list of strings
    print("\nRight-aligned list:")
    for string in string_list:
        print(format_string.format(string))
