'''Encrypt message
6 May 2014
Sydney Simpson'''

def encrypt(string):
    if len(string)==0:
        return string
    else:
        if not string.islower():
            return string[0]+encrypt(string[1:])
        else:
            if string[0]=="z":
                return "a"+encrypt(string[1:])
            elif string[0].isalpha():
                return chr(ord(string[0])+1)+encrypt(string[1:])
            else:
                return string[0]+encrypt(string[1:])
   
      
def function(string,number):
    if number==len(string)-1:
        return string[number]
    else:
        new= function(string,number+1)+string[number]
        return new
    
string= input("Enter a message:\n")
print("Encrypted message:")
new_string=(encrypt(string))
#print(function(new_string,0))
print(new_string)