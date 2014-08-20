'''Luke Joseph
2014-05-07
question 3 of assignment 8'''

# Function converting letters to one greater in the alphabet and z to a 
def encrypt(x):
    if x == "":
        return ""
    else:
        if x[0]=="z":
            return "a" + encrypt(x[1:])
        elif x[0].islower()==True:
            return chr(ord(x[0])+1)+ encrypt(x[1:])
        else:
            return x[0] + encrypt(x[1:])
        
# Main function printing outputs    
def main():
    x=input("Enter a message:\n")
    y=encrypt(x)
    print("Encrypted message:")
    print(y)
        
main()