value_str = input("Enter a string:\n")

if " " in value_str:
    values = value_str.replace(" ","")
else:
    values = value_str

tempvalue = values

palvalue = []

def palindrome(tempvalue):
    
    if len(tempvalue)==0:   
        return palvalue

    else:
        palvalue.append(tempvalue[-1])        
        palindrome(tempvalue[0:len(tempvalue)-1])
        
palindrome(values)

if values == "".join(palvalue):
    print("Palindrome!")
    
else:
    print("Not a palindrome!")